#Central configuration for the Macroinvertebrate Image Analysis System.
#Adapt DRIVE_BASE to match your Google Drive folder structure.

from pathlib import Path

# ── Google Drive root (update this if your folder name differs)
DRIVE_BASE = Path("/content/drive/MyDrive/macro_project")

# ── Data paths
DATA_DIR = DRIVE_BASE / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# ── Output paths (saved inside the cloned repo on Colab session storage)
REPO_BASE = Path("/content/macro_project")
OUTPUTS_DIR = REPO_BASE / "outputs"
EDA_OUTPUT_DIR = OUTPUTS_DIR / "eda"
MODEL_OUTPUT_DIR = OUTPUTS_DIR / "models"
REPORTS_OUTPUT_DIR = OUTPUTS_DIR / "reports"

# ── Image settings
IMAGE_SIZE = (128, 128)
SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp"}
