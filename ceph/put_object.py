import config
from client import s3

if __name__ == '__main__':
    with open('../data/test.png', 'rb') as file:
        data = file.read()

    response = s3.put_object(Bucket=config.BUCKET_NAME, Key=config.A_KEY, Body=data)
    print(response)
