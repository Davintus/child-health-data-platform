import sys  
from awsglue.transforms import *  
from awsglue.utils import getResolvedOptions  
from pyspark.context import SparkContext  
from awsglue.context import GlueContext  
from awsglue.job import Job  

args = getResolvedOptions(sys.argv, ['JOB_NAME'])  

glueContext = GlueContext(SparkContext.getOrCreate())  
spark = glueContext.spark_session  
job = Job(glueContext)  

# Reading from S3  
data_frame = glueContext.create_dynamic_frame.from_catalog(database="child_health_db", table_name="child_health_data")  

# Perform some transformation (for example, filtering)  
filtered_df = Filter.apply(frame=data_frame, f=lambda x: x["age"] > 5)  

# Writing back to S3  
glueContext.write_dynamic_frame.from_options(filtered_df, connection_type="s3", connection_options={"path": "s3://child-health-data-bucket/processed/"}, format="json")  

job.commit()
