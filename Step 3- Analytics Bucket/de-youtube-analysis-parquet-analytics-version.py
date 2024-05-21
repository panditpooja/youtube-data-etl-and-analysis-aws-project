import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1716298329538 = glueContext.create_dynamic_frame.from_catalog(database="de_youtube_cleaned", table_name="raw_statistics", transformation_ctx="AWSGlueDataCatalog_node1716298329538")

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1716298252980 = glueContext.create_dynamic_frame.from_catalog(database="de_youtube_cleaned", table_name="cleaned_statistics_reference_data", transformation_ctx="AWSGlueDataCatalog_node1716298252980")

# Script generated for node Join
Join_node1716298519068 = Join.apply(frame1=AWSGlueDataCatalog_node1716298329538, frame2=AWSGlueDataCatalog_node1716298252980, keys1=["category_id"], keys2=["id"], transformation_ctx="Join_node1716298519068")

# Script generated for node Amazon S3
AmazonS3_node1716298754800 = glueContext.getSink(path="s3://de-youtube-analytics-useast1-dev", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=["region", "category_id"], enableUpdateCatalog=True, transformation_ctx="AmazonS3_node1716298754800")
AmazonS3_node1716298754800.setCatalogInfo(catalogDatabase="db_analytics",catalogTableName="final_analystics")
AmazonS3_node1716298754800.setFormat("glueparquet", compression="snappy")
AmazonS3_node1716298754800.writeFrame(Join_node1716298519068)
job.commit()