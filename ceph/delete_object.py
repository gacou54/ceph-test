from ceph import config
from ceph.client import s3

if __name__ == '__main__':
    response = s3.delete_object(Bucket=config.BUCKET_NAME, Key=config.A_KEY)
    print(response)
