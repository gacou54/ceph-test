import requests

import config
from client import sns


def setup_http_subscription():
    return sns.subscribe(
        TopicArn=config.TOPIC_ARN,
        Protocol='https',
        Endpoint=f'http://{config.MY_IP}'
    )


def setup_amqp_subscription():
    return requests.put(
        f'/subscriptions/{config.SUB_NAME}'
        f'?topic={config.TOPIC_ARN}'
        f'?push-endpoint=amqp://{config.MY_IP}:5672&amqp-exchange={config.RABBITMQ_EXCHANGE}&amqp-ack-level=broker&verify-ssl=false'
    )


if __name__ == '__main__':
    # response = setup_http_subscription()
    response = setup_amqp_subscription()
