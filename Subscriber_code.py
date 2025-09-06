import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))

channel = connection.channel()

def callbacks(ch ,method ,properties ,body):
    print(body)


channel.basic_consume(queue='Q-1',on_message_callback=callbacks, auto_ack=True)

channel.start_consuming()

