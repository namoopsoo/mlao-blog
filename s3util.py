import boto3
import botocore
import os



s3conn = None
dataprovider_bucket = None

def set_conn():
    global s3conn
    s3conn = make_s3_resource()


def make_s3_resource():
    s3 = boto3.resource('s3',
            aws_access_key_id=os.getenv('S3_BLOG_UPLOAD_ACCESS_KEY'),
            aws_secret_access_key=os.getenv('S3_BLOG_UPLOAD_SECRET'),
            region_name=os.getenv('AWS_S3_REGION'))
    return s3


def write_s3_file(bucket_name, s3_filename, content):
    assert isinstance(content, basestring)
    try:
        s3conn.Object(bucket_name, s3_filename).put(
                Body=content)
        return True
    except botocore.exceptions.ClientError as e:
        return False


def read_s3_file(bucket_name, s3_filename):
    try:
        return s3conn.Object(bucket_name, s3_filename).get()["Body"].read()
    except botocore.exceptions.ClientError as e:
        return

