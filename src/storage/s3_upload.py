import boto3

def upload_to_s3(file_name, bucket):
    s3 = boto3.client("s3")
    s3.upload_file(file_name, bucket, file_name)
    print(f"✅ {file_name} uploaded to S3 bucket {bucket}")
