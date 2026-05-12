#Scans the raw dataset directory and builds a structured pandas DataFrame 
#where each row represents one indexed macroinvertebrate image.

from pathlib import Path

import cv2
import pandas as pd

from src.config import RAW_DATA_DIR, SUPPORTED_EXTENSIONS

class DatasetIndexer:
    """Scan the dataset folder and build a tabular image index.

    The indexer walks the raw data directory recursively and uses each
    image's parent folder name as its class label. This means your dataset
    inside data/raw/ should be organised as one subfolder per class, e.g.:

        data/raw/
        |-- mayfly/
        |   |-- img001.jpg
        |-- stonefly/
        |   |-- img002.jpg

    Attributes:
        data_dir: Path to the raw dataset directory.
    """

    def __init__(self, data_dir: Path = RAW_DATA_DIR) -> None:
        self.data_dir = data_dir

    def build_dataframe(self) -> pd.DataFrame:
        """Scan the dataset and return one row per valid image.

        Each row contains the file path, class label, width, height,
        and number of channels for one image.

        Returns:
            A pandas DataFrame with columns:
            file_path, label, width, height, channels.

        Raises:
            FileNotFoundError: If the dataset directory does not exist.
        """
        if not self.data_dir.exists():
            raise FileNotFoundError(
                f"Dataset directory not found: {self.data_dir}\n"
                "Make sure Google Drive is mounted and the path in config.py is correct."
            )

        records = []
        skipped = 0

        for file_path in self.data_dir.rglob("*"):
            if file_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
                continue

            image = cv2.imread(str(file_path))

            if image is None:
                skipped += 1
                continue

            height, width = image.shape[:2]
            channels = image.shape[2] if len(image.shape) == 3 else 1
            label = file_path.parent.name

            records.append(
                {
                    "file_path": str(file_path),
                    "label": label,
                    "width": width,
                    "height": height,
                    "channels": channels,
                }
            )

        if skipped > 0:
            print(f"Warning: {skipped} file(s) could not be read and were skipped.")

        print(f"Indexed {len(records)} images across the dataset.")
        return pd.DataFrame(records)
