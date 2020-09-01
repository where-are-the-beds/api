import boto3


def list_bucket():
    s3 = boto3.resource('s3')
    alist = []
    for bucket in s3.buckets.all():
        alist.append(bucket.name)
    return alist
