from pyspark.sql import SparkSession
from pyspark.sql.functions import (col, sha2)


def create_spark_session(appName="myApp"):
    """
    Function to create a spark session with hadoop 2.7.0 aws 
    configuration under the hood
    """

    spark = SparkSession \
        .builder \
        .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:2.7.0") \
        .appName(appName) \
        .getOrCreate()
    return spark


def process_customer_data(spark, input_data, output_data):
    """
    Function to read customer data from s3 bucket and 
    process that data using spark which is then annonymised and 
    written to csv files to a desired location
    """

    customer_data_filepath = input_data + "customerdata.csv"
    customer_data = spark.read.csv(customer_data_filepath, header=True)
    customer_data = customer_data.withColumn("first_name", sha2(customer_data.first_name, 256))\
           .withColumn("last_name", sha2(customer_data.last_name, 256))\
           .withColumn("address", sha2(customer_data.address, 256)) 


    customer_data.coalesce(3).write.save(output_data + "annonymised", header=True, format='csv')

if __name__ == "__main__":
    spark = create_spark_session(appName="dataProcessor")
    input_data = "s3a://nakuldefaultest/"

    #Note: The output s3 bucket should be in same region as emr cluster
    output_data = "s3://nakuldefaultest/" 
    process_customer_data(spark, input_data, output_data) 
    spark.stop()
