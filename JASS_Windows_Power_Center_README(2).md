# JASS Windows Power Center

**JASS Windows Power Center** is the central launcher/dashboard for the JASS Windows Toolkit.

Instead of opening individual `.py` files from Explorer, the Power Center automatically discovers JASS applications in its own folder and presents them in a modern desktop interface.

## Highlights

- Modern dark PySide6 interface
- Automatic discovery of `JASS_*.py` and `JASS_*.exe`
- Category-based navigation
- Search
- Favorites
- Recent-launch tracking
- One-click launching
- Automatic application descriptions
- Toolkit rescan
- Lightweight and local
- No central installation database required

## Screenshot concept

```text
┌──────────────────┬─────────────────────────────────────────────────┐
│ JASS             │ Windows Power Center             Sat 19 Sep     │
│ WINDOWS POWER    │ Your JASS toolkit, one beautiful control...     │
│ CENTER           │                                                 │
│                  │ ┌──────────────────────────────┐  ┌──────────┐  │
│ ⌂ All Tools      │ │ ⌕ Search JASS tools...      │  │ Sort     │  │
│ ▣ File & Folder  │ └──────────────────────────────┘  └──────────┘  │
│ ⚙ System         │                                                 │
│ ▤ Data & Database│ ┌──────────┐ ┌──────────┐ ┌──────────┐         │
│ ✦ Creative       │ │ Tool     │ │ Tool     │ │ Tool     │         │
│ ◈ Privacy        │ │ card     │ │ card     │ │ card     │         │
│ ⌘ Developer      │ │ Launch   │ │ Launch   │ │ Launch   │         │
│ ▰ Android        │ └──────────┘ └──────────┘ └──────────┘         │
│                  │                                                 │
│ ↻ Scan Toolkit   │ ┌──────────┐ ┌──────────┐ ┌──────────┐         │
│ ⓘ About          │ │ Tool     │ │ Tool     │ │ Tool     │         │
│                  │ └──────────┘ └──────────┘ └──────────┘         │
└──────────────────┴─────────────────────────────────────────────────┘
```

## Requirements

- Windows
- Python 3.10+
- PySide6

Install PySide6:

```powershell
py -m pip install PySide6
```

## Run

Place the Power Center in the same directory as your JASS applications and run:

```powershell
py JASS_Windows_Power_Center_v1.0.py
```

or:

```powershell
python JASS_Windows_Power_Center_v1.0.py
```

## How Discovery Works

The Power Center looks in its own directory for files matching:

```text
JASS_*.py
JASS_*.exe
```

The Power Center itself is excluded.

The application name is generated from the filename. For example:

```text
JASS_SQLite_Explorer_v1.7.0_fixed.py
```

appears approximately as:

```text
SQLite Explorer
```

## Categories

The first version automatically assigns tools to:

- File & Folder
- System
- Data & Database
- Creative
- Privacy & Security
- Developer
- Android & Apps
- Research
- Other

The classification is intentionally lightweight and based on filename keywords.

## Launching

Python applications are launched with the same Python interpreter running the Power Center:

```text
sys.executable
```

This is useful when the toolkit is being used inside a Python environment.

Executable applications (`.exe`) are launched directly through Windows.

The application's own directory is used as its working directory when launching Python applications.

## Favorites

Click the star on a tool card to add/remove it from Favorites.

Favorites are stored locally in:

```text
%APPDATA%\JASS\WindowsPowerCenter\power_center.json
```

## Rescan Toolkit

Use:

**↻ Scan Toolkit**

after adding a new JASS application to the repository.

The Power Center does not copy or modify discovered applications.

## Design Philosophy

The Power Center is intended to become the **front door of the JASS Windows Toolkit**.

Individual applications remain independent. The Power Center simply provides:

```text
Discover → Organize → Search → Launch
```

This keeps the toolkit modular while providing a unified desktop experience.

## Version

**v1.0 — Initial Power Center**

## Project

**JASS-Windows-Toolkit**
