# JASS PDF Toolkit v1.0

A lightweight Windows PDF utility built with PySide6 and PyMuPDF.

## Features

- Open and inspect PDF files
- Page list with text previews
- PDF metadata
- Merge multiple PDFs
- Extract selected pages
- Remove selected pages
- Rotate selected pages
- Reorder pages
- Search text across the PDF
- Open containing folder
- Background processing for longer operations
- Dark JASS interface
- Original source PDFs are not modified by the editing operations

## Requirements

- Windows
- Python 3.10+
- PySide6
- PyMuPDF

Install dependencies:

```powershell
py -m pip install PySide6 PyMuPDF
```

## Run

```powershell
py .\JASS_PDF_Toolkit_v1.0.py
```

## Reordering

Enter a complete page order using page numbers, for example:

```text
3,1,2,4
```

The example converts a four-page PDF from:

1, 2, 3, 4

to:

3, 1, 2, 4.

## Safety

Editing operations save to a new PDF selected by the user. The original PDF is not overwritten by the toolkit.

## Note

Text search works on text actually present in the PDF. Scanned/image-only PDFs require OCR and therefore may not produce searchable text.

## v1.1 Changes

- Uses the current `import pymupdf` API instead of deprecated `fitz`.
- Reworked background operations using Qt's `QThreadPool`/`QRunnable` pattern.
- Removed the previous QObject/QThread cleanup pattern that could produce cross-thread parent warnings.
