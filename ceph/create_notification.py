import config
from client import s3

response = s3.put_bucket_notification_configuration(
    Bucket=config.BUCKET_NAME,
    NotificationConfiguration={
        'TopicConfigurations': [
            {
                'Id': 'an-id',
                'TopicArn': config.TOPIC_ARN,
                'Events': [
                    's3:ObjectCreated:Put',
                ],
            },
        ],
    }
)
print(response)
