import os

# Base directory (1 level above the current file)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "."))

# Raw data file (CSV)
RAW_DATA_PATH = os.path.join(BASE_DIR, "raw_data", "predictive_maintenance.csv")

# Bronze and Silver layer paths (Parquet)
BRONZE_PATH = os.path.join(BASE_DIR, "blob_storage_simulation", "bronze", "predictive_maintenance.parquet")
SILVER_PATH = os.path.join(BASE_DIR, "blob_storage_simulation", "silver", "cleaned_data.parquet")
