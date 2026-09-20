# JASS INI Config Explorer v1.0

A lightweight configuration-file explorer and editor for INI-style files.

## Features

- Open `.ini`, `.cfg`, `.conf` and `.config`
- Section/key tree view
- Search sections, keys and values
- Case-sensitive search
- Inspect selected values
- Add sections
- Add keys
- Edit keys
- Delete keys with confirmation
- Raw INI editor
- Parse raw changes back into the structured view
- Normalize configuration formatting
- Save
- Save As
- Copy value
- Copy raw configuration
- Create a new INI document
- Dark JASS interface
- Uses Python standard library `configparser`

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
py .\JASS_INI_Config_Explorer_v1.0.py
```

## Notes

This utility targets INI-style configuration files. It intentionally uses Python's standard `configparser`, so it does not require an additional INI package.

Some vendor-specific configuration formats may use syntax that differs from standard INI conventions. Such files may not parse correctly.
