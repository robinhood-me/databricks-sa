import argparse

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, upper


parser = argparse.ArgumentParser()

parser.add_argument(
    "--input-path",
    default="dbfs:/tmp/people_from_notebook_csv"
)

args = parser.parse_args()

spark = SparkSession.builder.getOrCreate()

df = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "true")
    .csv(args.input_path)
)

processed_df = (
    df
    .withColumn("name_uppercase", upper(col("name")))
    .withColumn("age_next_year", col("age") + 1)
)

print("Original DataFrame from notebook:")
df.show()

print("Processed DataFrame from Python script:")
processed_df.show()