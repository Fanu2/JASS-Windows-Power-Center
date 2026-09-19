# JASS Folder Snapshot & Compare v1.0

A lightweight Windows utility for creating read-only folder snapshots and comparing a folder against an earlier snapshot.

## Features

- Recursive folder scanning
- Fast comparison using filename, file size and modified time
- SHA-256 verification mode for content-level comparison
- Detects:
  - New files
  - Deleted files
  - Modified files
  - Unchanged files
  - Renamed files (SHA-256 mode)
- Saved snapshots stored under:
  `%APPDATA%\JASS\FolderSnapshotCompare\snapshots`
- Progress reporting during scans
- Dark JASS-style PySide6 interface
- Export comparison reports as JSON, CSV or TXT
- Excludes common development/cache folders:
  `.git`, `__pycache__`, `.venv`, `venv`, `node_modules`, `build`, `dist`

## Requirements

- Windows
- Python 3.10+
- PySide6

Install PySide6 if needed:

```powershell
py -m pip install PySide6
```

## Run

```powershell
py .\JASS_Folder_Snapshot_Compare_v1.0.py
```

## How to use

1. Select a folder.
2. Choose **Fast** or **SHA-256 Verify**.
3. Click **Create Snapshot**.
4. Later, select the saved snapshot.
5. Select the same folder and click **Compare With Snapshot**.
6. Review the New, Deleted, Modified, Renamed and Unchanged tabs.
7. Export a report if required.

### Fast mode

Uses relative filename, file size and modification timestamp. It is much faster and is suitable for routine checks.

### SHA-256 Verify mode

Calculates a SHA-256 fingerprint for every file. This is slower but verifies file content rather than relying only on metadata.

### Rename detection

Rename detection is enabled in SHA-256 mode. If a deleted file and a newly added file have the same SHA-256 hash, the change is reported as a rename.

## Safety

The application is read-only with respect to the scanned folder. It does not delete, move, rename or modify files during scanning or comparison.

## Version

**v1.0**
