import config
from client import s3

if __name__ == '__main__':
    response = s3.get_object(Bucket=config.BUCKET_NAME, Key=config.A_KEY)

    with open('./data/tmp.png', 'wb') as file:
        file.write(response['Body'].read())

    print('done')
