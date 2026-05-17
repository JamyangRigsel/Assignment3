# Macroinvertebrate Image Analysis System

## Project Overview

This project is a Python-based image analysis system for freshwater macroinvertebrate image data.

The system focuses on:

- Stage 1: Exploratory Data Analysis
- Stage 3: Application Deployment

The project indexes macroinvertebrate image data, generates EDA visualisations, and provides a simple application interface for viewing the saved analysis outputs.

This project was completed for Software Technology 1 Assignment 3.

---
## Dataset
The project dataset was moved from google drive to this repostory after downsizing. 
System Design Summary
The system divides the code into separate modules and classes. Each having their own responsibility, making the project easier to understand, debug and maintain. 
Initially the dataset was stored in Google drive due to its large size, but after advice from the Professor, we downsized the dataset to 5 folders and moved them to Github. Stage 1 EDA was coded and completed in Google Colab and the outputs were saved into the repository. 
The stage 3 Tkinter App then used the outputs and presented them through a simple UI. Allowing users to choose what information they wanted to view. 


# Class and Module Overview
records.py:
This file contains the ImageRecord dataclass, which shows the metadata for an image. 
dataset_indexer.py:
It’s role is to scan the dataset and build a dataframe with Pandas. It searches through the raw data, finds the images that are supported and reads each image using OpenCV to extract information such as the image dimensions and channels. 
eda_service.py:
This generates the main analysis outputs. This class helps keep the EDA logic separate from the indexing logic. 
plotting.py:
Plotting functions that were used to make visual outputs such as the random image sample grids. 
main.py:
This file has the full Stage 1 EDA. It creates the directory for the output, indexes the dataset, runs the EDA and saves the outputs into the correct folder. 
app.py:
This file contains the Python code for the Tkinter UI app. Makes the output easy to access.


# Python Packages Used
Pathlib, OpenCV, Pandas, Matplotlib, Seaborn, Tkinter, Pillow. 
