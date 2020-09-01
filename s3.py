import boto3


def list_bucket():
    s3 = boto3.resource('s3')
    alist = []
    for bucket in s3.buckets.all():
        alist.append(bucket.name)
    return alist


def download_file():
    s3 = boto3.resource('s3')
    bucket = 'where-are-the-beds'
    key = 'usa-hospital-beds/dataset/usa-hospital-beds.csv'
    local_file_name = 'usa-hospital-beds.csv'

    s3.Bucket(bucket).download_file(key, local_file_name)
