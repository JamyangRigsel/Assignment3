"""Tkinter dashboard for viewing Stage 1 EDA outputs.

This application is the Stage 3 deployment component for the
Macroinvertebrate Image Analysis System. It displays the EDA charts
generated during Stage 1.
"""

import tkinter as tk
from pathlib import Path
from tkinter import messagebox

from PIL import Image, ImageTk


class MacroinvertebrateDashboard(tk.Tk):
    """Simple Tkinter dashboard for Stage 1 EDA outputs."""

    def __init__(self) -> None:
        super().__init__()

        self.title("Macroinvertebrate Image Analysis System")
        self.geometry("1000x700")
        self.resizable(False, False)

        # app.py is inside src/, so parent.parent goes back to repo root.
        self.project_root = Path(__file__).resolve().parent.parent
        self.eda_dir = self.project_root / "outputs" / "eda"

        self.current_image = None

        self.chart_files = {
            "Class Distribution": "class_distribution.png",
            "Class Imbalance": "class_imbalance.png",
            "Image Size Distribution": "image_size_distribution.png",
            "Channel Distribution": "channel_distribution.png",
            "Sample Image Grid": "sample_grid.png",
            "Class Sample Grid": "class_sample_grid.png",
        }

        self.build_ui()

    def build_ui(self) -> None:
        """Create the main dashboard layout."""

        title_label = tk.Label(
            self,
            text="Macroinvertebrate Image Analysis System",
            font=("Arial", 20, "bold"),
        )
        title_label.pack(pady=12)

        subtitle_label = tk.Label(
            self,
            text="Stage 3 Tkinter Dashboard for Stage 1 EDA Outputs",
            font=("Arial", 11),
        )
        subtitle_label.pack(pady=3)

        main_frame = tk.Frame(self)
        main_frame.pack(fill="both", expand=True, padx=15, pady=15)

        button_frame = tk.Frame(main_frame, width=220)
        button_frame.pack(side="left", fill="y", padx=(0, 15))

        instruction_label = tk.Label(
            button_frame,
            text="Choose an output:",
            font=("Arial", 12, "bold"),
        )
        instruction_label.pack(pady=(0, 10))

        for button_text, file_name in self.chart_files.items():
            button = tk.Button(
                button_frame,
                text=button_text,
                width=24,
                height=2,
                command=lambda name=file_name, title=button_text: self.show_chart(
                    name,
                    title,
                ),
            )
            button.pack(pady=5)

        about_button = tk.Button(
            button_frame,
            text="About Project",
            width=24,
            height=2,
            command=self.show_about,
        )
        about_button.pack(pady=(20, 5))

        exit_button = tk.Button(
            button_frame,
            text="Exit",
            width=24,
            height=2,
            command=self.destroy,
        )
        exit_button.pack(pady=5)

        display_frame = tk.Frame(
            main_frame,
            relief="solid",
            borderwidth=1,
            width=730,
            height=560,
        )
        display_frame.pack(side="right", fill="both", expand=True)
        display_frame.pack_propagate(False)

        self.chart_title_label = tk.Label(
            display_frame,
            text="Select an EDA output from the left menu",
            font=("Arial", 14, "bold"),
        )
        self.chart_title_label.pack(pady=10)

        self.image_label = tk.Label(
            display_frame,
            text="No chart selected",
            font=("Arial", 12),
        )
        self.image_label.pack(expand=True)

        self.status_label = tk.Label(
            self,
            text=f"Reading outputs from: {self.eda_dir}",
            font=("Arial", 9),
        )
        self.status_label.pack(pady=5)

    def show_chart(self, file_name: str, chart_title: str) -> None:
        """Load and display an EDA chart from the outputs/eda folder."""

        chart_path = self.eda_dir / file_name

        if not chart_path.exists():
            messagebox.showerror(
                "File not found",
                f"Could not find:\n\n{chart_path}\n\n"
                "Make sure the Colab EDA outputs have been pushed into "
                "outputs/eda.",
            )
            return

        image = Image.open(chart_path)

        # Resize the chart so it fits neatly inside the UI.
        image.thumbnail((700, 500))

        self.current_image = ImageTk.PhotoImage(image)

        self.chart_title_label.configure(text=chart_title)
        self.image_label.configure(image=self.current_image, text="")

    def show_about(self) -> None:
        """Show a short project explanation."""

        messagebox.showinfo(
            "About Project",
            "This application is the Stage 3 deployment component for the "
            "Macroinvertebrate Image Analysis System.\n\n"
            "The Stage 1 notebook generates EDA outputs such as class "
            "distribution, image size distribution, sample image grids, "
            "and channel distribution.\n\n"
            "This Tkinter dashboard loads those saved outputs from "
            "outputs/eda and displays them in a simple desktop interface.",
        )


def main() -> None:
    """Launch the Tkinter dashboard."""

    app = MacroinvertebrateDashboard()
    app.mainloop()


if __name__ == "__main__":
    main()
