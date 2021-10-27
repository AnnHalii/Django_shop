import pika
import json
from pymongo import MongoClient

credentials = pika.PlainCredentials(username='admin', password='admin')
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', 5672, '/', credentials))
channel = connection.channel()

channel.queue_declare(queue='click')

client = MongoClient('mongodb://admin:admin@mongodb:27017/?authSource=admin')
db = client.test_mongo
collection = db.some_app_register_click


def callback(ch, method, properties, body):
    print('Recieved')
    data = json.loads(body.decode('utf-8'))
    collection.insert_one({"username": data.get("username"), "timestamp": data.get("timestamp")}).inserted_id
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(queue='click', on_message_callback=callback)
channel.start_consuming()
