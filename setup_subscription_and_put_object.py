import config
from ceph.create_notification import create_sns_notification
from ceph.create_subscription import setup_amqp_subscription, setup_http_subscription
from ceph.create_topic import create_amqp_topic
from client import s3

print('Create topic')
response = create_amqp_topic(with_endpoint=False)

print('Create notification')
response = create_sns_notification()

print('Setup subscription')
response = setup_amqp_subscription()

print('Delete Object')
response = s3.delete_object(Bucket=config.BUCKET_NAME, Key=config.A_KEY)

print('Put object')
with open('./data/test.png', 'rb') as file:
    data = file.read()

response = s3.put_object(Bucket=config.BUCKET_NAME, Key=config.A_KEY, Body=data)
print(response)
