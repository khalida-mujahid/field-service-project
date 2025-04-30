from pyspark.sql import SparkSession
from config import BRONZE_PATH, SILVER_PATH

# Initialize Spark
spark = SparkSession.builder \
    .appName("ValidateDataQuality") \
    .config("spark.hadoop.io.native.lib.available", "false") \
    .config("spark.hadoop.fs.file.impl.disable.cache", "true") \
    .getOrCreate()

df_bronze = spark.read.load(BRONZE_PATH)
df_silver = spark.read.load(SILVER_PATH)

bronze_count = df_bronze.count()
silver_count = df_silver.count()

if silver_count / bronze_count < 0.9:
    print("Warning : Significant data loss during cleaning.")
else:
    print("Data Quality Validation Passed.")

spark.stop()
