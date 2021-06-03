from ceph.client import sns

if __name__ == '__main__':
    response = sns.list_topics()
    print(response)
