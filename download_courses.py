import os
from kaggle.api.kaggle_api_extended import KaggleApi
import zipfile
import pandas as pd

# Set up your Kaggle API credentials (optional if you already have kaggle.json)
os.environ['KAGGLE_USERNAME'] = "koludhanesh"  # Replace with your username
os.environ['KAGGLE_KEY'] = "b3062e26d0a0931e7eea409750dc88c2"  # Replace with your key

# Initialize the Kaggle API
api = KaggleApi()
api.authenticate()

# Define the dataset path (valid dataset)
dataset = "tianyimasf/coursera-course-dataset"  # Valid dataset path

# Download and unzip the dataset
try:
    api.dataset_download_files(dataset, path="data", unzip=True)
    print("✅ Dataset downloaded and extracted successfully.")
except Exception as e:
    print(f"❌ Error occurred while downloading dataset: {e}")

# Load and preview the dataset
try:
    df = pd.read_csv("data/coursera_courses.csv")
    print(df.head())  # Show first 5 records to verify data
except Exception as e:
    print(f"❌ Error occurred while loading the dataset: {e}")

# Optional: Save the cleaned version of the dataset (if needed)
try:
    df.to_csv("data/courses.csv", index=False)
    print("✅ Dataset saved as data/courses.csv")
except Exception as e:
    print(f"❌ Error occurred while saving the dataset: {e}")

