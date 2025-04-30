# Field Service ETL with PySpark and FastAPI

## Overview
A mini ETL project simulating Azure Blob Storage using local directories. Uses PySpark for pipeline and FastAPI for serving data.

## Setup Instructions
1. Create virtual environment
2. Install requirements:
    pip install -r requirements.txt

## Steps to Run
1. Download dataset into `raw_data/`
2. Run ETL pipeline:
    python etl_pipeline_script/create_bronze_silver.py
3. Validate data quality:
    python etl_pipeline_script/validate_data_quality.py
4. Run feature engineering notebook:
    Open `notebooks/feature_engineering.ipynb` and run cells.
5. Start API server:
    Run main.py