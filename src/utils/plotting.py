#Utility functions for generating visual outputs during EDA.

from pathlib import Path

import cv2
import matplotlib.pyplot as plt
import pandas as pd

def save_sample_grid(
    dataframe: pd.DataFrame,
    output_path: Path,
    sample_count: int = 9,
) -> None:
    """Save a grid of randomly sampled images for quick visual inspection.

    Args:
        dataframe:    The indexed image DataFrame from DatasetIndexer.
        output_path:  Full path (including filename) to save the grid image.
        sample_count: Number of images to include in the grid. Defaults to 9.
    """
    sample_df = dataframe.sample(
        min(sample_count, len(dataframe)), random_state=42
    )

    cols = 3
    rows = -(-len(sample_df) // cols)  # Ceiling division

    fig, axes = plt.subplots(rows, cols, figsize=(cols * 4, rows * 4))
    axes = axes.flat

    for ax, (_, row) in zip(axes, sample_df.iterrows()):
        image = cv2.imread(row["file_path"])
        if image is None:
            ax.axis("off")
            continue
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        ax.imshow(image)
        ax.set_title(row["label"], fontsize=9)
        ax.axis("off")

    # Turn off any leftover empty axes
    for ax in axes:
        ax.axis("off")

    plt.suptitle("Sample Images from Dataset", fontsize=13, y=1.01)
    plt.tight_layout()
    plt.savefig(output_path, bbox_inches="tight")
    plt.close()
    print(f"Saved: {output_path.name}")


def save_class_sample_grid(
    dataframe: pd.DataFrame,
    output_path: Path,
    samples_per_class: int = 3,
) -> None:
    """Save a grid showing a few sample images from every class.

    Useful for spotting visual differences between species at a glance.

    Args:
        dataframe:         The indexed image DataFrame from DatasetIndexer.
        output_path:       Full path (including filename) to save the grid.
        samples_per_class: How many images to show per class. Defaults to 3.
    """
    classes = dataframe["label"].unique()
    cols = samples_per_class
    rows = len(classes)

    fig, axes = plt.subplots(rows, cols, figsize=(cols * 3, rows * 3))

    # Ensure axes is always 2D even if only one class
    if rows == 1:
        axes = [axes]

    for row_idx, label in enumerate(classes):
        class_df = dataframe[dataframe["label"] == label].sample(
            min(samples_per_class, len(dataframe[dataframe["label"] == label])),
            random_state=42,
        )
        for col_idx in range(cols):
            ax = axes[row_idx][col_idx]
            if col_idx < len(class_df):
                image = cv2.imread(class_df.iloc[col_idx]["file_path"])
                if image is not None:
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                    ax.imshow(image)
                    if col_idx == 0:
                        ax.set_ylabel(label, fontsize=8, rotation=0, labelpad=60)
            ax.axis("off")

    plt.suptitle("Sample Images per Class", fontsize=13, y=1.01)
    plt.tight_layout()
    plt.savefig(output_path, bbox_inches="tight")
    plt.close()
    print(f"Saved: {output_path.name}")
