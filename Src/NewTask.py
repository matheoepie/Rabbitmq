import sys, pika

connecion = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connecion.channel()

channel.queue_declare(queue='', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))
print(" [x] Sent %r" % message)

connecion.close()