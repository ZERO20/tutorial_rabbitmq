#! /usr/bin/env python

import pika


parameters = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(parameters=parameters)
channel = connection.channel()

channel.queue_declare(queue='hello') # create a queue

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!') # Send message
print(" [x] Sent 'Hello World!'")

connection.close() # Closing the connection
