#Data model for a single indexed macroinvertebrate image.

from dataclasses import dataclass
from pathlib import Path

@dataclass
class ImageRecord:
    """Store the core metadata for one indexed macroinvertebrate image.
    Attributes:
        file_path: Absolute path to the image file.
        label:     Class name derived from the parent folder name.
        width:     Image width in pixels.
        height:    Image height in pixels.
        channels:  Number of colour channels (1 for grayscale, 3 for RGB).
    """

    file_path: Path
    label: str
    width: int
    height: int
    channels: int
