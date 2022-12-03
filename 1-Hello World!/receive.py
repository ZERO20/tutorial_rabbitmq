import os, sys

import pika

from functions import callback


def main():
    parameters = pika.ConnectionParameters(host='localhost')
    connection = pika.BlockingConnection(parameters=parameters)
    channel = connection.channel()
    """
        Creating a queue using queue_declare is idempotent,
        we can run the command as many times as we like, and only one will be created
    """
    channel.queue_declare(queue='hello') # create a queue

    # to receive messages from a queue we need a callback function
    channel.basic_consume(queue='hello', auto_ack=True, on_message_callback=callback)
    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
