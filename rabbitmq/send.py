import pika

import config

if __name__ == '__main__':
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=config.MY_IP)
    )
    channel = connection.channel()

    # channel.queue_declare(queue=config.RABBITMQ_QUEUE)
    channel.queue_declare(queue=config.RABBITMQ_QUEUE + 'tmp')

    channel.basic_publish(exchange='', routing_key=config.RABBITMQ_QUEUE + 'tmp', body=b'Hello World!')
    print(" [x] Sent 'Hello World!'")
    connection.close()
