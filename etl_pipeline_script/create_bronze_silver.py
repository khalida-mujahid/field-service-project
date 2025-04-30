from pyspark.sql import SparkSession
from config import RAW_DATA_PATH, BRONZE_PATH, SILVER_PATH


def init_spark(app_name: str = "FieldServiceETL") -> SparkSession:
    return SparkSession.builder \
        .appName(app_name) \
        .config("spark.hadoop.io.native.lib.available", "false") \
        .config("spark.hadoop.fs.file.impl.disable.cache", "true") \
        .getOrCreate()


def ingest_raw_data(spark: SparkSession, input_path: str):
    print(f"Reading raw data from: {input_path}")
    return spark.read.csv(input_path, header=True, inferSchema=True)


def write_parquet(df, output_path: str, layer_name: str):
    try:
        df.write.mode("overwrite").parquet(output_path)
        print(f"{layer_name} write successful at: {output_path}")
    except Exception as e:
        print(f"Error during {layer_name} write: {e}")


def transform_bronze_to_silver(df_bronze):
    # Apply transformations ( drop nulls)
    return df_bronze.dropna()


def main():
    print("Starting ETL Process...")
    print(f"RAW_DATA_PATH: {RAW_DATA_PATH}")
    print(f"BRONZE_PATH: {BRONZE_PATH}")
    print(f"SILVER_PATH: {SILVER_PATH}")

    spark = init_spark()

    # Bronze Layer
    df_raw = ingest_raw_data(spark, RAW_DATA_PATH)
    write_parquet(df_raw, BRONZE_PATH, "Bronze")

    # Silver Layer
    try:
        df_bronze = spark.read.parquet(BRONZE_PATH)
        df_silver = transform_bronze_to_silver(df_bronze)
        write_parquet(df_silver, SILVER_PATH, "Silver")
    except Exception as e:
        print("Error during Silver layer transformation:", e)

    spark.stop()
    print("ETL Process Completed.")


if __name__ == "__main__":
    main()
