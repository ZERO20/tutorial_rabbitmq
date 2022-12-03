# Tutorial for RabbitMQ with Python

[Official documentation](https://www.rabbitmq.com/getstarted.html)
___


## 1 - "Hello World!"

Send and receive messages in a queue

~~~
# Read message
python receive.py

# Sent message
python send.py
~~~
___



## Notes

### Listing queues
You may wish to see what queues RabbitMQ has and how many messages are in them. You can do it (as a privileged user) using the rabbitmqctl tool:

```
sudo rabbitmqctl list_queues

On Windows, omit the sudo:

rabbitmqctl.bat list_queues
```