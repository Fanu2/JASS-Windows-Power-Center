# JASS Media Inventory v1.0

A lightweight, read-only media cataloging utility for images, videos and audio files.

## Features

- Recursive media scanning
- Images, videos and audio classification
- Filename and path search
- Filter by media type
- File size and modified date
- Optional FFprobe metadata
- Video/audio duration
- Video resolution
- Codec and container/format where FFprobe is available
- Media totals by category
- Total media size
- Access-error count
- Double-click to open a media file
- Open selected file location
- Export to JSON, CSV or TXT
- Background scanning
- Dark JASS interface

## Supported formats

### Images
JPG/JPEG, PNG, GIF, BMP, TIFF, WEBP, ICO, SVG, HEIC/HEIF, AVIF

### Video
MP4, MKV, AVI, MOV, WMV, WEBM, M4V, MPEG/MPG, TS, M2TS, 3GP

### Audio
MP3, WAV, FLAC, AAC, M4A, OGG/OGA, WMA, OPUS, MIDI

## Optional FFprobe metadata

Basic inventory information works without FFmpeg.

If `ffprobe.exe` is available in your PATH, choose **FFprobe metadata** to obtain additional video/audio information such as duration, codec, resolution, channels and sample rate.

For example, if FFmpeg is already installed:

```powershell
ffprobe -version
```

No FFmpeg installation is required for the basic mode.

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
py .\JASS_Media_Inventory_v1.0.py
```

## Safety

The application is read-only. It does not delete, move, rename, transcode or modify media files.

## Version

**v1.0**
