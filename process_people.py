import argparse

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, upper


parser = argparse.ArgumentParser()

parser.add_argument(
    "--table-name",
    default="workspace.default.people_from_notebook"
)

args = parser.parse_args()

spark = SparkSession.builder.getOrCreate()

df = spark.table(args.table_name)

processed_df = (
    df
    .withColumn("name_uppercase", upper(col("name")))
    .withColumn("age_next_year", col("age") + 1)
)

print("Original DataFrame from notebook table:")
df.show()

print("Processed DataFrame from Python script:")
processed_df.show()