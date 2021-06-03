import config
from client import sns

if __name__ == '__main__':
    response = sns.create_topic(
        Name=config.TOPIC,
        Attributes={
            'push-endpoint': config.ENDPOINT,
            'verify-ssl': 'false',
        }
    )
    print(response)
