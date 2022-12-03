def callback(ch, method, properties, body):
    """Callback for receiving messages from a queue"""
    print(" [x] Received %r" % body)