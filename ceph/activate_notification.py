from ceph import config
from ceph.client import s3


response = s3.put_bucket_notification_configuration(
    Bucket=config.BUCKET_NAME,
    NotificationConfiguration={
        'TopicConfigurations': [
            {
                'Id': 'an-id',
                'TopicArn': 'arn:aws:sns:ul::a-topic',
                'Events': [
                    's3:ObjectCreated:Put',
                    's3:ObjectRemoved:Delete'
                ],
            },
        ],
    }
)