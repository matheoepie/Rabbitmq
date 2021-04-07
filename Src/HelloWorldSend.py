import pika

connecion = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connecion.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(
    exchange='',
    routing_key='hello',
    body='Hello world')

print(" [x] send 'Hello World'")

connecion.close()