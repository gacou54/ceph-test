import pika

import config

if __name__ == '__main__':
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=config.RABBITMQ_IP)
    )
    channel = connection.channel()

    channel.exchange_declare(exchange=config.RABBITMQ_EXCHANGE, exchange_type='fanout')

    channel.basic_publish(exchange=config.RABBITMQ_EXCHANGE, routing_key='', body=b'Hello World!')
    print(" [x] Sent 'Hello World!'")
    connection.close()
