from pyspark.sql import SparkSession
#from delta import *

if __name__ == "__main__":
    spark = (
        SparkSession
        .builder
        .appName("ConvertToParquet")
        .getOrCreate())

    mnm_file = "/mnt/data/mnm_dataset.csv"

    mnm_df = (
        spark.read.format("csv")
        .option("header", "true")
        .option("inferSchema", "true")
        .load(mnm_file))

    path = "/mnt/data/mnm_parquet"
    mnm_df.write.format("parquet").save(path)
