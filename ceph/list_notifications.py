import config
from client import s3

if __name__ == '__main__':
    response = s3.get_bucket_notification_configuration(
        Bucket=config.BUCKET_NAME,
    )

    print(response)
