#Generates and saves exploratory data analysis outputs for the indexed macroinvertebrate image dataset.

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

class EDAService:
    """Generate and save EDA outputs for the indexed image dataset.
    Attributes:
        dataframe:  The indexed image DataFrame from DatasetIndexer.
        output_dir: Directory where all EDA outputs will be saved.
    """

    def __init__(self, dataframe: pd.DataFrame, output_dir: Path) -> None:
        self.dataframe = dataframe
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def save_class_distribution(self) -> None:
        """Save a bar chart showing the number of images per class."""
        order = self.dataframe["label"].value_counts().index

        plt.figure(figsize=(14, 6))
        sns.countplot(data=self.dataframe, x="label", order=order, palette="viridis")
        plt.xticks(rotation=45, ha="right")
        plt.title("Macroinvertebrate Images per Class", fontsize=14)
        plt.xlabel("Class")
        plt.ylabel("Image Count")
        plt.tight_layout()
        plt.savefig(self.output_dir / "class_distribution.png")
        plt.close()
        print("Saved: class_distribution.png")

    def save_image_size_distribution(self) -> None:
        """Save width and height distribution histograms side by side."""
        fig, axes = plt.subplots(1, 2, figsize=(12, 5))

        sns.histplot(self.dataframe["width"], bins=20, ax=axes[0], color="steelblue")
        sns.histplot(self.dataframe["height"], bins=20, ax=axes[1], color="coral")

        axes[0].set_title("Image Width Distribution")
        axes[1].set_title("Image Height Distribution")
        axes[0].set_xlabel("Width (px)")
        axes[1].set_xlabel("Height (px)")

        plt.tight_layout()
        plt.savefig(self.output_dir / "image_size_distribution.png")
        plt.close()
        print("Saved: image_size_distribution.png")

    def save_class_imbalance_chart(self) -> None:
        """Save a horizontal bar chart to make class imbalance easy to spot."""
        counts = self.dataframe["label"].value_counts()

        plt.figure(figsize=(10, 8))
        counts.plot(kind="barh", color="mediumseagreen")
        plt.title("Class Imbalance Overview", fontsize=14)
        plt.xlabel("Image Count")
        plt.ylabel("Class")
        plt.tight_layout()
        plt.savefig(self.output_dir / "class_imbalance.png")
        plt.close()
        print("Saved: class_imbalance.png")

    def save_channel_distribution(self) -> None:
        """Save a count plot showing how many images are RGB vs grayscale."""
        plt.figure(figsize=(6, 4))
        sns.countplot(data=self.dataframe, x="channels", palette="Set2")
        plt.title("Image Channel Distribution (1=Grayscale, 3=RGB)")
        plt.xlabel("Channels")
        plt.ylabel("Count")
        plt.tight_layout()
        plt.savefig(self.output_dir / "channel_distribution.png")
        plt.close()
        print("Saved: channel_distribution.png")

    def build_summary(self) -> dict:
        """Return key dataset summary statistics as a dictionary.

        Returns:
            A dict containing total image count, class count,
            mean width, and mean height.
        """
        summary = {
            "total_images": int(len(self.dataframe)),
            "total_classes": int(self.dataframe["label"].nunique()),
            "mean_width": round(float(self.dataframe["width"].mean()), 2),
            "mean_height": round(float(self.dataframe["height"].mean()), 2),
            "min_width": int(self.dataframe["width"].min()),
            "max_width": int(self.dataframe["width"].max()),
            "min_height": int(self.dataframe["height"].min()),
            "max_height": int(self.dataframe["height"].max()),
        }
        return summary

    def print_summary(self) -> None:
        """Print a formatted dataset summary to the console."""
        summary = self.build_summary()
        print("\n── Dataset Summary ──────────────────────────")
        for key, value in summary.items():
            print(f"  {key:<20}: {value}")
        print("─────────────────────────────────────────────\n")

    def run_all(self) -> None:
        """Generate and save all EDA outputs in one call."""
        self.save_class_distribution()
        self.save_image_size_distribution()
        self.save_class_imbalance_chart()
        self.save_channel_distribution()
        self.print_summary()
        print("All EDA outputs saved.")
