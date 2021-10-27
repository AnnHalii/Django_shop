import pika
import json


def publish(data):
    credentials = pika.PlainCredentials(username='admin', password='admin')
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', 5672, '/', credentials))
    channel = connection.channel()

    channel.queue_declare(queue='click')
    channel.basic_publish(exchange='', routing_key='click', body=json.dumps(data).encode('utf-8'))
