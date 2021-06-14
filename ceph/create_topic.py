import config
from client import sns


def create_http_topic():
    return sns.create_topic(
        Name=config.TOPIC_NAME,
        Attributes={
            'push-endpoint': f'http://{config.MY_IP}:8000',
            'verify-ssl': 'false',
        }
    )


def create_amqp_topic():
    return sns.create_topic(
        Name=config.TOPIC_NAME,
        Attributes={
            'push-endpoint': f'amqp://{config.MY_IP}:5672',
            'amqp-exchange': '',
            'amqp-ack-level': 'broker',
        }
    )


if __name__ == '__main__':
    response = create_http_topic()
    # response = create_amqp_topic()
    print(response)
