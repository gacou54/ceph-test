from ceph import config
from ceph.client import s3

if __name__ == '__main__':
    response = s3.create_bucket(Bucket=config.BUCKET_NAME)
    print(response)
