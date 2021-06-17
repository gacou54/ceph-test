import config
from client import sns


def setup_subscription():
    return sns.subscribe(
        TopicArn=config.TOPIC_ARN,
        Protocol='https',
        Endpoint=f'http://{config.MY_IP}'
    )


if __name__ == '__main__':
    response = setup_subscription()
