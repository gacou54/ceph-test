from client import s3

if __name__ == '__main__':
    response = s3.list_buckets()

    for item in response['Buckets']:
        print(item['CreationDate'], item['Name'])
