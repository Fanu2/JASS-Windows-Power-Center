# JASS Windows Services Inspector v1.0

A lightweight Windows service inspection and control utility built with PySide6.

## Features

- Lists Windows services using Windows CIM
- Service name and display name
- Running / stopped state
- Automatic / manual / disabled startup type
- Service account
- Executable / service path
- Service description
- Search across service metadata
- Filter by state
- Filter by startup type
- Start a stopped service
- Stop a running service
- Restart a service
- Explicit confirmation before service control
- Service details
- Service dependencies and dependents
- Export complete inventory to CSV
- Background scanning so the interface remains responsive
- Dark JASS-style interface

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
py .\JASS_Windows_Services_Inspector_v1.0.py
```

## Notes

Some service-control operations require an elevated PowerShell / administrator session.

The application does not change service startup types in v1.0. It only provides Start, Stop and Restart controls with explicit confirmation.

## Safety

Starting, stopping or restarting a Windows service can affect Windows components or installed applications. Use the Details and Dependencies views before changing a service.

## Version

**v1.0**
