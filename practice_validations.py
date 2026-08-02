import os
from pyspark.sql import SparkSession
import great_expectations as gx
import pandas as pd
import pytest

from pyspark.sql import SparkSession

# 1. Check Great Expectations Version
print(f"Great Expectations version: {gx.__version__}")

# 2. Check Spark Version
# If you already have an active Spark Session:
spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

# Suppress the NativeCodeLoader warning specifically via Java loggers
log4j = spark._jvm.org.apache.log4j
log4j.LogManager.getLogger("org.apache.hadoop.util.NativeCodeLoader").setLevel(
    log4j.Level.ERROR
)
print(f"Spark version (via session): {spark.version}")

# Alternatively, check via the underlying pyspark module version:
import pyspark

print(f"PySpark library version: {pyspark.__version__}")

print(f"Pandas library version: {pd.__version__}")
print(f"Pytest library verion:{pytest.__version__}")
