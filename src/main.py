from pathlib import Path

from src.config import EDA_OUTPUT_DIR, RAW_DATA_DIR
from src.services.dataset_indexer import DatasetIndexer
from src.services.eda_service import EDAService
from src.utils.plotting import save_sample_grid, save_class_sample_grid

def main() -> None:
    """Run the full Stage 1 EDA pipeline."""

    # Create output directory if it doesn't exist yet
    EDA_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # ── Step 1: Index the dataset
    print("Indexing dataset...")
    indexer = DatasetIndexer(data_dir=RAW_DATA_DIR)
    dataframe = indexer.build_dataframe()

    if dataframe.empty:
        print("No images found. Check that your dataset path is correct.")
        return

    # ── Step 2: Run EDA
    print("\nRunning EDA...")
    eda = EDAService(dataframe=dataframe, output_dir=EDA_OUTPUT_DIR)
    eda.run_all()

    # ── Step 3: Save sample image grids
    print("\nGenerating sample image grids...")
    save_sample_grid(
        dataframe=dataframe,
        output_path=EDA_OUTPUT_DIR / "sample_grid.png",
        sample_count=9,
    )
    save_class_sample_grid(
        dataframe=dataframe,
        output_path=EDA_OUTPUT_DIR / "class_sample_grid.png",
        samples_per_class=3,
    )

    print("\nStage 1 EDA complete. All outputs saved to:", EDA_OUTPUT_DIR)

if __name__ == "__main__":
    main()
