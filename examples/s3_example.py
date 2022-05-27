import os
import json
import boto3

cfile = open("/home/vishvaraj/configs/aws_opcito.json", 'r')
configs = json.loads(cfile.read())

# s3 create bucket
s3_r = boto3.client(
    "s3",
    region_name="us-east-1"
)

# s3_r.create_bucket(
#     ACL="private",
#     Bucket="test-bucket-1",
#     CreateBucketConfiguration={
#         "LocationConstraint": "us-east-2"
#     }
# )
# rr = s3_r.create_bucket(Bucket="test-py-bucket2")
# print(rr)

# list s3 buckets
# response = s3_r.list_buckets()
# for bucket in response['Buckets']:
#     print(bucket['Name'])


# delete s3 buckets test-aws-s3-bkt1
rrr = s3_r.delete_bucket(Bucket="test-py-bucket2")
print(rrr)

