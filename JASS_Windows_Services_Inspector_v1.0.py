import sys
import os
import json
import csv
import subprocess
from pathlib import Path

from PySide6.QtCore import Qt, QObject, QThread, Signal, Slot
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem,
    QHeaderView, QMessageBox, QComboBox, QFileDialog, QAbstractItemView,
    QProgressBar, QCheckBox
)

APP_NAME = "JASS Windows Services Inspector"
APP_VERSION = "1.0"

STYLE = """
QWidget {
    background:#11151b; color:#e7edf5;
    font-family:"Segoe UI"; font-size:10pt;
}
QMainWindow { background:#0d1117; }
QLabel#Title { font-size:22pt; font-weight:700; color:#ffffff; }
QLabel#SubTitle { color:#8d99a8; }
QLineEdit,QComboBox,QTableWidget {
    background:#171c23; border:1px solid #303947;
    border-radius:7px; padding:7px; color:#e7edf5;
}
QComboBox QAbstractItemView {
    background:#171c23; color:#e7edf5;
    selection-background-color:#263d59;
}
QPushButton {
    background:#202936; border:1px solid #354254;
    border-radius:7px; padding:8px 13px;
}
QPushButton:hover { background:#293545; }
QPushButton#Primary {
    background:#245b8f; border-color:#347ab9; font-weight:700;
}
QPushButton#Danger { background:#44252a; border-color:#67353c; }
QTableWidget { gridline-color:#252d38; selection-background-color:#263d59; }
QHeaderView::section {
    background:#1c232d; color:#aeb9c7; padding:7px; border:0;
}
QProgressBar {
    background:#171c23; border:1px solid #303947;
    border-radius:6px; height:16px; text-align:center;
}
QProgressBar::chunk { background:#347ab9; border-radius:5px; }
"""

def ps_json(script):
    p = subprocess.run(
        ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", script],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
        creationflags=subprocess.CREATE_NO_WINDOW
    )
    if p.returncode != 0:
        raise RuntimeError(p.stderr.strip() or "PowerShell command failed.")
    out = p.stdout.strip()
    if not out:
        return []
    try:
        data = json.loads(out)
    except json.JSONDecodeError:
        return []
    return data if isinstance(data, list) else [data]

def get_services():
    script = r"""
Get-CimInstance Win32_Service |
Select-Object Name,DisplayName,State,StartMode,StartName,PathName,Description |
ConvertTo-Json -Depth 4
"""
    return ps_json(script)

def service_command(action, name):
    safe = name.replace("'", "''")
    script = f"""
try {{
    $svc = Get-Service -Name '{safe}' -ErrorAction Stop
    {action} -Name '{safe}' -ErrorAction Stop
    Write-Output 'OK'
}} catch {{
    Write-Error $_.Exception.Message
    exit 1
}}
"""
    p = subprocess.run(
        ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", script],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
        creationflags=subprocess.CREATE_NO_WINDOW
    )
    if p.returncode != 0:
        raise RuntimeError(p.stderr.strip() or f"Unable to {action.lower()} service.")

class ScanWorker(QObject):
    finished = Signal(object)
    failed = Signal(str)

    @Slot()
    def run(self):
        try:
            self.finished.emit(get_services())
        except Exception as e:
            self.failed.emit(str(e))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(f"{APP_NAME} v{APP_VERSION}")
        self.resize(1450, 820)
        self.setMinimumSize(1050, 650)
        self.setStyleSheet(STYLE)
        self.services = []
        self.filtered = []
        self.thread = None
        self.worker = None
        self.build_ui()
        self.scan()

    def build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        root = QVBoxLayout(central)
        root.setContentsMargins(20,18,20,15)
        root.setSpacing(11)

        title = QLabel(APP_NAME)
        title.setObjectName("Title")
        sub = QLabel("Inspect Windows services, startup types, executable paths and dependencies.")
        sub.setObjectName("SubTitle")
        root.addWidget(title)
        root.addWidget(sub)

        bar = QHBoxLayout()
        self.search = QLineEdit()
        self.search.setPlaceholderText("Search service name, description, path or account…")
        self.search.textChanged.connect(self.apply_filter)
        bar.addWidget(self.search, 1)

        self.state_filter = QComboBox()
        self.state_filter.addItems(["All states", "Running", "Stopped"])
        self.state_filter.currentTextChanged.connect(self.apply_filter)
        bar.addWidget(self.state_filter)

        self.start_filter = QComboBox()
        self.start_filter.addItems(["All startup types", "Auto", "Manual", "Disabled"])
        self.start_filter.currentTextChanged.connect(self.apply_filter)
        bar.addWidget(self.start_filter)

        refresh = QPushButton("Refresh")
        refresh.setObjectName("Primary")
        refresh.clicked.connect(self.scan)
        bar.addWidget(refresh)

        export = QPushButton("Export CSV")
        export.clicked.connect(self.export_csv)
        bar.addWidget(export)

        root.addLayout(bar)

        self.progress = QProgressBar()
        self.progress.setRange(0,0)
        self.progress.setVisible(False)
        root.addWidget(self.progress)

        self.table = QTableWidget(0, 8)
        self.table.setHorizontalHeaderLabels([
            "Service", "Display Name", "State", "Startup", "Account",
            "Executable / Path", "Description", "Actions"
        ])
        headers = self.table.horizontalHeader()
        headers.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        headers.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        headers.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        headers.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        headers.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        headers.setSectionResizeMode(5, QHeaderView.Stretch)
        headers.setSectionResizeMode(6, QHeaderView.Stretch)
        headers.setSectionResizeMode(7, QHeaderView.ResizeToContents)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        root.addWidget(self.table, 1)

        bottom = QHBoxLayout()
        self.status = QLabel("Loading services…")
        self.status.setObjectName("SubTitle")
        bottom.addWidget(self.status, 1)

        details = QPushButton("Details")
        details.clicked.connect(self.show_details)
        bottom.addWidget(details)

        deps = QPushButton("Dependencies")
        deps.clicked.connect(self.show_dependencies)
        bottom.addWidget(deps)

        root.addLayout(bottom)

    def scan(self):
        if self.thread and self.thread.isRunning():
            return
        self.progress.setVisible(True)
        self.status.setText("Reading Windows service database…")
        self.thread = QThread()
        self.worker = ScanWorker()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.scan_finished)
        self.worker.failed.connect(self.scan_failed)
        self.worker.finished.connect(self.thread.quit)
        self.worker.failed.connect(self.thread.quit)
        self.thread.finished.connect(self.scan_done)
        self.thread.start()

    def scan_done(self):
        self.progress.setVisible(False)
        self.worker = None
        self.thread = None

    def scan_failed(self, msg):
        self.progress.setVisible(False)
        self.status.setText("Service scan failed.")
        QMessageBox.critical(self, "Service Scan Error", msg)

    def scan_finished(self, services):
        self.services = services
        self.apply_filter()

    def apply_filter(self):
        text = self.search.text().strip().lower()
        state = self.state_filter.currentText()
        startup = self.start_filter.currentText()

        self.filtered = []
        for s in self.services:
            st = str(s.get("State", ""))
            sm = str(s.get("StartMode", ""))
            hay = " ".join(str(s.get(k, "")) for k in (
                "Name","DisplayName","Description","PathName","StartName"
            )).lower()

            state_ok = state == "All states" or st.lower() == state.lower()
            start_ok = startup == "All startup types" or sm.lower() == startup.lower()

            if state_ok and start_ok and (not text or text in hay):
                self.filtered.append(s)

        self.table.setRowCount(0)

        for s in self.filtered:
            row = self.table.rowCount()
            self.table.insertRow(row)

            vals = [
                s.get("Name",""),
                s.get("DisplayName",""),
                s.get("State",""),
                s.get("StartMode",""),
                s.get("StartName",""),
                s.get("PathName",""),
                s.get("Description","") or "",
            ]
            for col, value in enumerate(vals):
                item = QTableWidgetItem(str(value))
                if col == 2:
                    item.setTextAlignment(Qt.AlignCenter)
                self.table.setItem(row, col, item)

            actions = QWidget()
            al = QHBoxLayout(actions)
            al.setContentsMargins(2,2,2,2)
            al.setSpacing(4)

            state_value = str(s.get("State",""))
            if state_value.lower() == "running":
                stop = QPushButton("Stop")
                stop.clicked.connect(lambda checked=False, x=s: self.control_service(x, "Stop-Service"))
                al.addWidget(stop)
            else:
                start = QPushButton("Start")
                start.clicked.connect(lambda checked=False, x=s: self.control_service(x, "Start-Service"))
                al.addWidget(start)

            restart = QPushButton("Restart")
            restart.clicked.connect(lambda checked=False, x=s: self.control_service(x, "Restart-Service"))
            al.addWidget(restart)

            self.table.setCellWidget(row, 7, actions)

        self.status.setText(f"{len(self.filtered)} shown • {len(self.services)} total")

    def selected_service(self):
        row = self.table.currentRow()
        if row < 0 or row >= len(self.filtered):
            return None
        return self.filtered[row]

    def control_service(self, service, action):
        name = service.get("Name", "")
        label = action.replace("-Service", "")
        reply = QMessageBox.question(
            self,
            f"{label} Service",
            f"{label} this Windows service?\n\n"
            f"Service: {name}\n"
            f"Display name: {service.get('DisplayName','')}\n\n"
            "Changing service state can affect Windows or installed applications.",
            QMessageBox.Yes | QMessageBox.No,
        )
        if reply != QMessageBox.Yes:
            return

        try:
            service_command(action, name)
            self.scan()
        except Exception as e:
            QMessageBox.critical(self, "Service Control Error", str(e))

    def show_details(self):
        s = self.selected_service()
        if not s:
            QMessageBox.information(self, "Details", "Select a service first.")
            return

        text = (
            f"Service name:\n{s.get('Name','')}\n\n"
            f"Display name:\n{s.get('DisplayName','')}\n\n"
            f"State: {s.get('State','')}\n"
            f"Startup type: {s.get('StartMode','')}\n"
            f"Account: {s.get('StartName','')}\n\n"
            f"Executable / Path:\n{s.get('PathName','')}\n\n"
            f"Description:\n{s.get('Description','') or '(none)'}"
        )
        QMessageBox.information(self, "Service Details", text)

    def show_dependencies(self):
        s = self.selected_service()
        if not s:
            QMessageBox.information(self, "Dependencies", "Select a service first.")
            return

        name = s.get("Name", "").replace("'", "''")
        script = f"""
$svc = Get-Service -Name '{name}' -ErrorAction Stop
[PSCustomObject]@{{
    Required = @($svc.ServicesDependedOn | Select-Object -ExpandProperty Name)
    Dependents = @($svc.DependentServices | Select-Object -ExpandProperty Name)
}} | ConvertTo-Json -Depth 4
"""
        try:
            data = ps_json(script)
            data = data[0] if data else {}
            required = data.get("Required", [])
            dependents = data.get("Dependents", [])
            if isinstance(required, str): required = [required]
            if isinstance(dependents, str): dependents = [dependents]

            text = (
                f"Service: {s.get('Name','')}\n\n"
                "Requires:\n" + ("\n".join(required) if required else "(none)") +
                "\n\nOther services depending on it:\n" +
                ("\n".join(dependents) if dependents else "(none)")
            )
            QMessageBox.information(self, "Service Dependencies", text)
        except Exception as e:
            QMessageBox.warning(self, "Dependency Error", str(e))

    def export_csv(self):
        if not self.services:
            QMessageBox.information(self, "Export", "No service data available.")
            return

        path, _ = QFileDialog.getSaveFileName(
            self, "Export Services Report",
            "JASS_Windows_Services_Report.csv",
            "CSV (*.csv)"
        )
        if not path:
            return

        try:
            with open(path, "w", newline="", encoding="utf-8-sig") as f:
                w = csv.writer(f)
                w.writerow([
                    "Service","Display Name","State","Startup Type",
                    "Account","Executable / Path","Description"
                ])
                for s in self.services:
                    w.writerow([
                        s.get("Name",""),
                        s.get("DisplayName",""),
                        s.get("State",""),
                        s.get("StartMode",""),
                        s.get("StartName",""),
                        s.get("PathName",""),
                        s.get("Description","") or "",
                    ])
            QMessageBox.information(self, "Export Complete", f"Report saved to:\n{path}")
        except Exception as e:
            QMessageBox.critical(self, "Export Error", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName(APP_NAME)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
