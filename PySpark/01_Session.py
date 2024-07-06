'''
For Pysark we always need to create a session
'''

import pyspark
from pyspark import SparkContext
from pyspark.sql import SparkSession

sc = SparkContext('local')
spark = SparkSession.builder.appName('Test_py').getOrCreate()
print(spark)

df_pyspark = spark.read.csv('PySpark\creditcard_2023.csv')
print(df_pyspark)

# To use same headers as the csv file
df_pyspark = spark.read.option('header','true').csv('PySpark\creditcard_2023.csv')
print(df_pyspark)

print(df_pyspark.show())

print(df_pyspark.printSchema())

print(df_pyspark.head())