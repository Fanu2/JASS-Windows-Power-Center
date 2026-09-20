# JASS Windows Power Centre

A collection of lightweight, practical Windows desktop utilities built with **Python + PySide6**.

The **JASS Windows Power Centre** is designed as a growing personal toolkit for file management, document inspection, data exploration, system diagnostics, creative work, and everyday Windows productivity.

The applications are intentionally modular: each utility can be run independently and most tools require only Python and PySide6, with additional packages used only where a particular format requires them.

---

## ✨ Toolkit Highlights

- Modern dark JASS-branded interfaces
- Standalone Python applications
- Windows-focused
- Local-first and privacy-friendly
- Read-only design wherever practical
- Background scanning for larger operations
- SQLite-based local catalogs where useful
- CSV / JSON / TXT export in many tools
- No cloud account required
- No central server required
- Lightweight dependencies
- Each application can be used independently

---

# 📦 Applications

## 1. JASS Document Cataloger

A document inventory and cataloging utility.

### Features

- Recursively scan document folders
- PDF
- Word / OpenDocument
- Excel / CSV / TSV
- PowerPoint / OpenDocument
- TXT / Markdown / RTF
- EPUB / MOBI / AZW / AZW3
- HTML / XML / JSON
- Search filename and path
- Filter by document category
- File size and modification date
- Open documents
- Open containing folder
- Persistent SQLite catalog
- CSV export
- Background scanning
- Access-error reporting

---

## 2. JASS EPUB Library Manager

A dedicated local ebook library manager.

### Features

- Recursively scan ebook folders
- EPUB metadata extraction
- Title
- Author
- Publisher
- Language
- Publication date
- Identifier / ISBN
- Description
- Subjects / categories
- Chapter information
- File size
- SHA-256 hash
- Embedded cover preview
- Search title, author, identifier and subjects
- Language filtering
- Sorting
- Duplicate identification through hashes
- Open ebook with the default reader
- CSV export
- JSON export
- Persistent SQLite library

### EPUB Support

Full metadata support is provided for EPUB.

MOBI, AZW and AZW3 can also be inventoried.

---

## 3. JASS Folder Snapshot & Compare

A folder comparison and change-detection utility.

### Features

- Create recursive folder snapshots
- Fast comparison mode
- SHA-256 verification mode
- Detect:
  - New files
  - Deleted files
  - Modified files
  - Unchanged files
- Detect renamed files in hash verification mode
- Persistent snapshots
- Progress reporting
- TXT / CSV / JSON export
- Development/cache directory exclusions
- Read-only scanning

---

## 4. JASS Folder Statistics Studio

Analyze the contents and size distribution of folders.

### Features

- Recursive folder analysis
- File count
- Folder count
- Total size
- Largest files
- File-type statistics
- Folder-level statistics
- Percentage of total size
- Hidden-file handling
- Access-error reporting
- TXT / CSV / JSON export
- Background scanning
- Read-only operation

---

## 5. JASS INI Config Explorer

Explore and edit INI-style configuration files.

### Features

- Open `.ini`
- Open `.cfg`
- Open `.conf`
- Open `.config`
- Section/key tree
- Search sections, keys and values
- Case-sensitive search
- Inspect selected values
- Add sections
- Add keys
- Edit values
- Delete keys
- Raw INI editor
- Parse raw changes
- Normalize formatting
- Save / Save As
- Copy values and configuration
- Create new INI files

Uses Python's standard-library `configparser`.

---

## 6. JASS Image Metadata Explorer

Inspect image properties and metadata.

### Features

- Recursive image scanning
- Open individual images
- JPEG
- PNG
- TIFF
- WebP
- BMP
- GIF
- ICO
- Common image formats
- Dimensions
- File size
- Format and color mode
- EXIF metadata
- Camera make/model
- Date taken
- Lens
- ISO
- Aperture
- Shutter speed
- Focal length
- Orientation
- Software / creator metadata
- GPS information when present
- Image preview
- Metadata search
- Image-type filtering
- CSV / JSON export

### Dependency

```powershell
py -m pip install Pillow
```

---

## 7. JASS JSON Explorer

A structured JSON inspection and editing utility.

### Features

- Open JSON files
- Create new JSON documents
- Expandable object/array tree
- Direct JSON editing
- Key/value search
- Find / Find Next
- Case-sensitive search
- JSON validation
- Pretty formatting
- Compact/minified JSON
- Save / Save As
- Selected-value viewer
- Copy selected values
- Unsaved-change protection
- UTF-8 support

---

## 8. JASS Media Inventory

Catalog images, videos and audio files.

### Features

- Recursive media scanning
- Images
- Videos
- Audio
- Search filename/path
- Filter by media type
- File size
- Modified date
- Optional FFprobe metadata
- Video/audio duration
- Video resolution
- Codec
- Container
- Counts
- Total size
- Access-error reporting
- Double-click to open
- Open containing folder
- CSV / JSON / TXT export
- Background scanning
- Read-only operation

### Optional FFmpeg / FFprobe

Basic inventory operation works without FFmpeg.

FFprobe can provide richer media metadata when available.

---

## 9. JASS PDF Toolkit

A practical PDF inspection and manipulation utility.

### Features

- Open PDFs
- Inspect metadata
- Page list
- Text previews
- Search text
- Merge PDFs
- Extract selected pages
- Remove selected pages
- Rotate pages
- Reorder pages
- Open containing folder
- Background processing
- Dark JASS interface

Editing operations create output documents rather than modifying the original source PDFs.

### Dependency

PyMuPDF is used through the modern `pymupdf` package.

```powershell
py -m pip install PyMuPDF
```

---

## 10. JASS Romance Studio

A private, local-first romantic interactive-fiction and creative-writing studio.

### Features

- Character creator
- Relationship setting
- Romantic scene builder
- Multiple settings
- Multiple scene types
- Mood controls:
  - Tender
  - Romantic
  - Flirty
  - Sensual
  - Intimate
- Romantic tension control
- Interactive scene continuation
- Suggested next moments
- Romance prompt deck
- Love-letter generator
- Date-idea generator
- Scene history
- Save/load story files
- TXT export

### Story Format

Stories use the local:

```text
.jrs.json
```

format.

The v1.0 creative experience focuses on adult romance, affection, atmosphere, dialogue and sensual relationship tension rather than explicit sexual content.

---

## 11. JASS SQLite Explorer

A lightweight SQLite database explorer.

### Features

- Open `.db`
- Open `.sqlite`
- Open `.sqlite3`
- Create new SQLite databases
- Browse tables
- Filter table names
- Inspect table schema
- View table data
- Load up to 10,000 rows
- Search loaded rows
- Run read-only `SELECT` queries
- View query results
- Show schema SQL
- Copy schema
- Export table data to CSV
- Database size information
- Table count

### Safety

Existing databases are intentionally read-only in v1.0.

The explorer does not execute:

- `INSERT`
- `UPDATE`
- `DELETE`
- `DROP`
- `ALTER`

---

## 12. JASS System Inspector

A Windows system and development-environment diagnostic utility.

### Features

- Windows/system overview
- CPU information
- CPU cores and threads
- CPU usage
- RAM information
- GPU information
- Drive capacity and free space
- Network adapters
- Python detection
- Git detection
- Node.js detection
- npm detection
- PowerShell detection
- Docker detection
- Ollama detection
- Tool versions and paths
- Copy diagnostics
- TXT / JSON export
- Refresh

The tool uses lightweight Windows/PowerShell information sources rather than requiring a heavy system-monitoring dependency.

---

## 13. JASS Text File Analyzer

Analyze text-based files and logs.

### Features

- TXT
- Markdown
- LOG
- Other text files
- Encoding detection
- File size
- Line count
- Empty/non-empty line counts
- Word count
- Unique word count
- Character count
- Non-whitespace character count
- Paragraph count
- Average line length
- Longest line
- Shortest line
- Duplicate-line detection
- Most frequent words
- Text viewer
- Normal search
- Case-sensitive search
- Regular-expression search
- Match highlighting
- TXT / JSON / CSV reports
- Background analysis
- Read-only operation

---

## 14. JASS Windows Power Center

A central launcher and dashboard for JASS utilities.

### Features

- JASS-branded dashboard
- Sidebar categories
- Search
- Favorites
- Tool cards
- Launch applications
- Scan Toolkit
- Application Sources
- Toolkit statistics
- Automatic discovery of `JASS_*.py`
- Automatic discovery of `JASS_*.exe`
- Recursive source scanning
- Configurable external source folders

Application sources are stored under:

```text
%APPDATA%\JASS\WindowsPowerCenter\
```

---

## 15. JASS Windows Services Inspector

Inspect and manage Windows services.

### Features

- Windows service inventory
- Service name
- Display name
- Running/stopped state
- Startup type
- Service account
- Executable path
- Description
- Search/filter
- Start service
- Stop service
- Restart service
- Dependencies
- Dependents
- CSV export
- Background scanning

Service-changing operations require confirmation.

---

## 16. JASS Windows Startup Manager

Inspect applications and tasks that start with Windows.

### Features

- Registry Run entries
- HKCU startup entries
- HKLM startup entries
- WOW6432Node startup entries
- User Startup folder
- All Users Startup folder
- Logon-triggered Scheduled Tasks
- Search/filter
- Details
- Inventory backup
- CSV export
- Open locations
- Disable selected scheduled tasks with confirmation
- Background scanning

Registry startup entries are treated as read-only in v1.0.

---

## 17. JASS Portable App Manager

Manage a personal collection of portable Windows applications.

### Features

- Add portable-app folders
- Recursive `.exe` discovery
- Automatic name/category suggestions
- Search
- Favorites
- Launch applications
- Open application folders
- Add/edit/remove entries
- Rescan
- CSV export
- Persistent JSON catalog

Catalog data is stored under:

```text
%APPDATA%\JASS\PortableAppManager\
```

---

## 18. JASS System Diagnostics

A generated diagnostic snapshot can be used alongside the System Inspector and other troubleshooting utilities to record the current Windows environment.

---

# 🛠️ Common Requirements

Most applications require:

- Windows 10/11
- Python 3.10+
- PySide6

Install the main GUI dependency:

```powershell
py -m pip install PySide6
```

Additional packages are required only for particular applications.

### EbookLib

For EPUB Library Manager:

```powershell
py -m pip install EbookLib
```

### Pillow

For Image Metadata Explorer:

```powershell
py -m pip install Pillow
```

### PyMuPDF

For PDF Toolkit:

```powershell
py -m pip install PyMuPDF
```

---

# ▶️ Running an Application

From the directory containing the application:

```powershell
py .\JASS_JSON_Explorer_v1.0.py
```

For example:

```powershell
py .\JASS_SQLite_Explorer_v1.0.py
```

or:

```powershell
py .\JASS_Romance_Studio_v1.0.py
```

---

# 📁 Suggested Repository Structure

A clean repository can be organized like this:

```text
JASS-Windows-Toolkit/
│
├── README.md
│
├── JASS_Document_Cataloger_v1.0.py
├── JASS_Document_Cataloger_README.md
│
├── JASS_EPUB_Library_Manager_v1.0.py
├── JASS_EPUB_Library_Manager_README.md
│
├── JASS_Folder_Snapshot_Compare_v1.0.py
├── JASS_Folder_Snapshot_Compare_README.md
│
├── JASS_Folder_Statistics_Studio_v1.0.py
├── JASS_Folder_Statistics_Studio_README.md
│
├── JASS_INI_Config_Explorer_v1.0.py
├── JASS_INI_Config_Explorer_README.md
│
├── JASS_Image_Metadata_Explorer_v1.0.py
├── JASS_Image_Metadata_Explorer_README.md
│
├── JASS_JSON_Explorer_v1.0.py
├── JASS_JSON_Explorer_README.md
│
├── JASS_Media_Inventory_v1.0.py
├── JASS_Media_Inventory_README.md
│
├── JASS_PDF_Toolkit_v1.1.py
├── JASS_PDF_Toolkit_README.md
│
├── JASS_Romance_Studio_v1.0.py
├── JASS_Romance_Studio_README.md
│
├── JASS_SQLite_Explorer_v1.0.py
├── JASS_SQLite_Explorer_README.md
│
├── JASS_System_Inspector_v1.0.py
├── JASS_System_Inspector_README.md
│
├── JASS_Text_File_Analyzer_v1.0.py
├── JASS_Text_File_Analyzer_README.md
│
├── JASS_Windows_Power_Center_v1.1.py
├── JASS_Windows_Power_Center_README.md
│
├── JASS_Windows_Services_Inspector_v1.0.py
├── JASS_Windows_Services_Inspector_README.md
│
├── JASS_Windows_Startup_Manager_v1.0.py
├── JASS_Windows_Startup_Manager_README.md
│
├── JASS_Portable_App_Manager_v1.0.py
└── JASS_Portable_App_Manager_README.md
```

---

# 🔒 Design Philosophy

The JASS Windows Toolkit follows a few simple principles:

### Local First

Applications operate on the user's own Windows machine whenever possible.

### Privacy First

There is no requirement to upload personal documents, databases, photographs or stories to a cloud service.

### Lightweight

The toolkit avoids unnecessary heavyweight frameworks and dependencies.

### Independent Utilities

Each application should remain useful on its own rather than requiring the entire toolkit.

### Read-Only Where Practical

Inspection and cataloging applications avoid modifying the source material.

### Explicit Actions

Operations that can change system state or user data use explicit controls and, where appropriate, confirmation dialogs.

### Practical Over Complex

The goal is to solve real everyday problems without turning every utility into a large software platform.

---

# 🧪 Development

Applications are developed and tested incrementally.

Typical development workflow:

1. Define the utility's purpose
2. Keep dependencies minimal
3. Build the PySide6 interface
4. Implement the core operation
5. Add safety checks
6. Add export/persistence where useful
7. Syntax-check the Python source
8. Test on Windows
9. Freeze a stable version
10. Add the next independent utility

---

# 🚀 Roadmap

Possible future additions include:

- More document and ebook tools
- Archive Explorer
- Markdown Library Manager
- Subtitle Library Manager
- Image Duplicate Finder
- Video Metadata Explorer
- Font Explorer
- Windows Environment Variable Explorer
- Local Application Launcher improvements
- JASS Toolkit packaging
- Portable toolkit distribution
- Optional integration with local AI through Ollama / LM Studio

AI integration, where added, will remain optional rather than being a requirement for the basic utilities.

---

# 📜 License

Choose and add the repository's preferred license before public distribution.

---

## JASS Windows Toolkit

**Practical Windows utilities.  
Local-first. Lightweight. Private. Modular.**
