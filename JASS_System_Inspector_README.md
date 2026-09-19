# JASS System Inspector

A lightweight Windows system-information and diagnostics dashboard from the JASS Windows Toolkit.

## Features

- Windows version/build information
- Computer name and architecture
- CPU model, cores, threads and maximum clock
- Live CPU usage
- RAM installed, used and available
- Live memory usage
- GPU information
- Drive capacity, free space and usage
- Network adapter information
- Python detection
- Git detection
- Node.js detection
- npm detection
- PowerShell detection
- Docker detection
- Ollama detection
- Copy diagnostics to clipboard
- Export TXT report
- Export JSON report
- Automatic refresh of live CPU/RAM information

## Requirements

- Windows
- Python 3.10+
- PySide6

Install PySide6:

```powershell
py -m pip install PySide6
```

## Run

```powershell
py .\JASS_System_Inspector_v1.0.py
```

## Design

The application intentionally uses Python's standard library and built-in Windows PowerShell/CIM commands rather than heavy system-information packages.

This keeps the utility lightweight and suitable for machines where installing large dependencies is undesirable.

## Report

A diagnostic report can be exported as:

```text
JASS_System_Diagnostics_YYYY-MM-DD_HHMMSS.txt
```

or as JSON.

The report can be useful when troubleshooting JASS applications because it records the machine and development environment.

## Safety

The inspector is read-only. It does not modify system settings, services, files, applications or registry entries.

## Version

**v1.0 — Initial release**

Part of **JASS-Windows-Toolkit**.
