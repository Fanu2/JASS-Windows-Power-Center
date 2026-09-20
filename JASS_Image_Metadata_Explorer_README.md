# JASS Image Metadata Explorer v1.0

A lightweight PySide6 utility for inspecting image properties and EXIF metadata.

## Features

- Scan an entire image folder recursively
- Open a single image
- JPEG, PNG, TIFF, WebP, BMP, GIF and other common formats
- Image dimensions
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
- Software/creator metadata
- GPS coordinates when present
- Thumbnail preview
- Search metadata
- Filter by image type
- Export CSV
- Export JSON
- Background folder scanning
- Read-only operation
- Dark JASS interface

## Requirements

- Windows
- Python 3.10+
- PySide6
- Pillow

Install:

```powershell
py -m pip install PySide6 Pillow
```

## Run

```powershell
py .\JASS_Image_Metadata_Explorer_v1.0.py
```

## Privacy

The application reads metadata locally. It does not upload images or metadata anywhere.

GPS coordinates, if present in an image's EXIF data, are displayed and exported because they are part of the image metadata. Treat exported metadata files accordingly.

## Safety

The original images are never modified.
