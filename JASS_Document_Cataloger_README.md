# JASS Document Cataloger v1.0

A lightweight local document inventory and search utility built with PySide6 and SQLite.

## Features

- Recursively catalog common document formats
- PDF
- Word / OpenDocument
- Excel / CSV / TSV
- PowerPoint / OpenDocument presentations
- TXT / Markdown / RTF
- EPUB / MOBI / AZW / AZW3
- HTML / XML / JSON
- Search by filename, path or extension
- Filter by document category
- Optional inclusion of other file types
- File size and modification date
- Full path information
- Double-click/open document
- Open containing folder
- Persistent local SQLite catalog
- CSV export
- Background scanning
- Access-error reporting
- Dark JASS interface

## Catalog database

The catalog is stored locally at:

```text
%APPDATA%\JASS\DocumentCataloger\document_catalog.db
```

The database is automatically refreshed when **Scan / Update Catalog** is run.

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
py .\JASS_Document_Cataloger_v1.0.py
```

## Safety

The cataloger is read-only with respect to scanned documents. It does not rename, move, delete or modify documents.

The SQLite catalog is separate from the scanned folders.

## Version

**v1.0**
