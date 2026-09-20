# JASS EPUB Library Manager v1.0

A local-first ebook library manager focused on EPUB metadata.

## Features

- Recursively scan ebook folders
- EPUB metadata extraction
- Title and author
- Publisher
- Language
- Publication date
- Identifier / ISBN when supplied by the EPUB
- Description
- Subjects/categories
- Chapter/item count
- File size and modification date
- SHA-256 hash
- Search title, author, ISBN/identifier, subjects, description and path
- Filter by language
- Sort by title, author, date or size
- EPUB cover preview when an embedded image is available
- Open ebook with the Windows default application
- Export CSV
- Export JSON
- Persistent SQLite library
- Background scanning
- Read-only operation
- Dark JASS interface

## Ebook Formats

### Full metadata support
- `.epub`

### Inventory support
- `.mobi`
- `.azw`
- `.azw3`

MOBI/AZW/AZW3 files are cataloged by filename, size, path and hash in v1.0. EPUB metadata extraction is handled through EbookLib.

## Requirements

- Windows
- Python 3.10+
- PySide6
- EbookLib

Install:

```powershell
py -m pip install PySide6 EbookLib
```

## Run

```powershell
py .\JASS_EPUB_Library_Manager_v1.0.py
```

## Library Database

The persistent catalog is stored at:

```text
%APPDATA%\JASS\EPUBLibraryManager\epub_library.db
```

The database is separate from the ebook files.

## Safety and Privacy

- Original ebooks are never modified.
- Scanning is local.
- No ebook content or metadata is uploaded anywhere.
- SHA-256 hashes are calculated locally.
