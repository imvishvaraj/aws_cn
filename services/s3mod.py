import boto3


class S3MOD:
    def __init__(self, region_name):
        self.service_name = "s3"
        self.s3obj = boto3.client(self.service_name, region_name=region_name)

    def list_buckets(self):
        try:
            buckets = []
            res = self.s3obj.list_buckets()
            for bucket in res['Buckets']:
                buckets.append(bucket['Name'])
            return buckets
        except Exception as ee:
            return {"error": str(ee)}

    def create(self, bucket_name):
        try:
            return self.s3obj.create_bucket(Bucket=bucket_name)
        except Exception as ee:
            return {"error": str(ee)}

    def delete(self, bucket_name):
        try:
            return self.s3obj.delete_bucket(Bucket=bucket_name)
        except Exception as ee:
            return {"error": str(ee)}