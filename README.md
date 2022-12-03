# Tutorial for RabbitMQ with Python

[Official documentation](https://www.rabbitmq.com/getstarted.html)
___


## Content

1. ["Hello World!"](</1-Hello World!>)

___

## Notes

### Listing queues
You may wish to see what queues RabbitMQ has and how many messages are in them. You can do it (as a privileged user) using the rabbitmqctl tool:

```
sudo rabbitmqctl list_queues

On Windows, omit the sudo:

rabbitmqctl.bat list_queues
```