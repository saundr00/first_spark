from __future__ import print_function
from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = (SparkSession
        .builder
        .appName("PythonMnMCount")
        .master("spark://Bobbys-MBP.fios-router.home:7077")
        .getOrCreate())

    mnm_file = "data/mnm_delta"

    mnm_df = (spark.read.format("delta")
        .load(mnm_file))
    mnm_df.show(n=5, truncate=False)

    count_mnm_df = (mnm_df.select("State", "Color", "Count")
                    .groupBy("State", "Color")
                    .sum("Count")
                    .orderBy("sum(Count)", ascending=False))

    count_mnm_df.show(n=60, truncate=False)
    print("Total Rows = %d" % (count_mnm_df.count()))

    ca_count_mnm_df = (mnm_df.select("*")
                       .where(mnm_df.State == 'AZ')
                       .groupBy("State", "Color")
                       .sum("Count")
                       .orderBy("sum(Count)", ascending=False))

    ca_count_mnm_df.show(n=10, truncate=False)

