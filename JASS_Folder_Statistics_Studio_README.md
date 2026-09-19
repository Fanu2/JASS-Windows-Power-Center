# JASS Folder Statistics Studio v1.0

A lightweight, read-only folder analysis utility for understanding where disk space is being used.

## Features

- Recursive folder analysis
- Total file count
- Total folder count
- Total size
- Largest files
- File-type statistics by extension
- Folder-level size statistics
- Percentage of total space
- Hidden-file inclusion option
- Access-error count
- Search-free, straightforward reporting
- Background scanning so large folders do not freeze the interface
- Export to JSON, CSV or TXT
- Excludes common development/cache directories:
  `.git`, `__pycache__`, `.venv`, `venv`, `node_modules`, `build`, `dist`
- Dark JASS interface

## Safety

The application is read-only. It does not delete, move, rename or modify files.

## Requirements

- Windows
- Python 3.10+
- PySide6

Install PySide6 if required:

```powershell
py -m pip install PySide6
```

## Run

```powershell
py .\JASS_Folder_Statistics_Studio_v1.0.py
```

## Report formats

- **JSON** — complete structured analysis
- **CSV** — file-type and folder statistics suitable for Excel
- **TXT** — human-readable report

## Version

**v1.0**
