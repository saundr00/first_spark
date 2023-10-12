from pyspark.sql import SparkSession
from delta import *
import os

if __name__ == "__main__":
    spark = (
        SparkSession
        .builder
        .appName("ConvertToDelta")
        .getOrCreate())

    mnm_file = os.path.join(os.environ["DATA_DIR"], "mnm_dataset.csv")

    mnm_df = (
        spark.read.format("csv")
        .option("header", "true")
        .option("inferSchema", "true")
        .load(mnm_file))

    path = os.path.join(os.environ["DATA_DIR"], "mnm_delta")
    mnm_df.write.format("delta").partitionBy("State").save(path)
