import config
from client import sns

if __name__ == '__main__':
    response = sns.delete_topic(TopicArn=config.TOPIC_ARN)
    print(response)
