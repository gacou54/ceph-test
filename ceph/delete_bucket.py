import config
from client import s3

if __name__ == '__main__':
    response = s3.delete_bucket(Bucket=config.BUCKET_NAME)
    print(response)
