# JASS SQLite Explorer v1.0

A lightweight, read-only SQLite database explorer for the JASS toolkit.

## Features

- Open existing SQLite databases
- Create a new empty SQLite database
- Browse tables
- Filter table names
- Inspect table schema
- View table data
- Load up to 10,000 rows at a time
- Search loaded rows
- Run read-only `SELECT` SQL queries
- Display query results
- Show/copy table schema SQL
- Export loaded table data to CSV
- Database file size and table count
- Dark JASS interface
- No external database server required

## Supported Files

- `.db`
- `.sqlite`
- `.sqlite3`

## Requirements

- Windows
- Python 3.10+
- PySide6

Install:

```powershell
py -m pip install PySide6
```

## Run

```powershell
py .\JASS_SQLite_Explorer_v1.0.py
```

## Safety

v1.0 is intentionally read-only for existing databases:

- No INSERT
- No UPDATE
- No DELETE
- No DROP
- No ALTER
- No schema modification

The only database creation operation is **New Database**, which creates an empty SQLite file selected by the user.

## Notes

Large tables are loaded in batches using the selected row limit. The row search operates on the rows currently loaded into the table view.

This utility is useful for inspecting databases created by other JASS applications, including SQLite catalogs and research databases.
