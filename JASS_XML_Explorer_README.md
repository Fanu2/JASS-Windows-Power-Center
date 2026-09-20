# JASS XML Explorer v1.0

A lightweight XML inspection and editing utility for the JASS toolkit.

## Features

- Open XML documents
- New XML document
- Save XML
- XML structure tree
- Element text inspection
- Attribute inspection
- Child count
- Search elements, attributes and text
- Case-sensitive search option
- XML validation
- Pretty/format XML
- Copy XML to clipboard
- Supports XML, XSD, SVG, RSS and Atom documents
- Dark JASS interface
- Standard-library XML parser
- No external XML package required

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
py .\JASS_XML_Explorer_v1.0.py
```

## Safety

The application works locally. Opening and inspecting documents is read-only; saving only occurs when the user explicitly selects Save.

## Note

v1.0 validates XML for well-formedness. It does not perform XSD schema validation.
