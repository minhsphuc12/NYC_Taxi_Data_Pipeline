import os
from minio import Minio
from minio.commonconfig import REPLACE, CopySource
from minio.error import S3Error

client = Minio('localhost:9025', access_key='admin', secret_key='password', secure=False)
client.get_bucket_versioning('test1').status
bucket_name = 'testbucket-python'

if not client.bucket_exists(bucket_name=bucket_name):
    client.make_bucket(bucket_name)
    print(f'bucket {bucket_name} is created.')
else:
    print(f'bucket {bucket_name} already exists.')

file_path = '/Users/phucnm/git/misc/NYC_Taxi_Data_Pipeline/minhsphuc12/data/fhv_tripdata_2019-11.parquet'
object_name = 'fhv_tripdata_2019-11.parquet'
client.fput_object(bucket_name=bucket_name, object_name=object_name, file_path=file_path)

# Function to optimize upload using multipart upload
# def optimized_upload(client, bucket_name, object_name, file_path):
#     file_stat = os.stat(file_path)
#     file_size = file_stat.st_size

#     # Define part size (e.g., 5MB)
#     part_size = 5 * 1024 * 1024

#     # Upload the file
#     try:
#         with open(file_path, 'rb') as file_data:
#             client.put_object(
#                 bucket_name, 
#                 object_name, 
#                 file_data, 
#                 file_size,
#                 part_size=part_size,
#                 content_type="application/octet-stream"
#             )
#         print(f"File '{file_path}' uploaded as '{object_name}' in bucket '{bucket_name}'.")
#     except S3Error as e:
#         print(f"Error occurred: {e}")

# Call the optimized upload function
# optimized_upload(client, bucket_name, object_name, file_path)


metadata = client.stat_object(bucket_name=bucket_name, object_name=object_name)
metadata.size, metadata.last_modified, metadata.etag, metadata.content_type

new_object_name = 'test_new_name_object'
client.copy_object(bucket_name, new_object_name, CopySource(bucket_name, object_name))
client.remove_object(bucket_name=bucket_name, object_name=new_object_name)

