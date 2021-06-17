import config
from client import s3


def create_sns_notification():
    """Crée une notification simple"""
    return s3.put_bucket_notification_configuration(
        Bucket=config.BUCKET_NAME,
        NotificationConfiguration={
            'TopicConfigurations': [
                {
                    'Id': config.AN_ID,
                    'TopicArn': config.TOPIC_ARN,
                    'Events': [
                        's3:ObjectCreated:Put',
                    ],
                },
            ],
        }
    )


def create_sqs_notification():
    """Crée une notification "queue" """
    return s3.put_bucket_notification_configuration(
        Bucket=config.BUCKET_NAME,
        NotificationConfiguration={
            'QueueConfigurations': [
                {
                    'Id': 'an-id',
                    'QueueArn': config.TOPIC_ARN,
                    'Events': [
                        's3:ObjectCreated:Put',
                    ],
                },
            ],
        }
    )


if __name__ == '__main__':
    response = create_sns_notification()

    print(response)
