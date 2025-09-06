import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))  # creating a connection

channel = connection.channel()  # channel has all the functionalities to use rabbitmq

# create a exchange

channel.exchange_declare(exchange = 'Nikitha_talkz', exchange_type='direct')

# create queue or queues

channel.queue_declare(queue='Q-1')
channel.queue_declare(queue='Q-2')
channel.queue_declare(queue='Q-3')

# binding the exchange and queues

channel.queue_bind(queue='Q-1', exchange='Nikitha_talkz', routing_key='movies')
channel.queue_bind(queue='Q-2', exchange='Nikitha_talkz', routing_key='short films')
channel.queue_bind(queue='Q-3', exchange='Nikitha_talkz', routing_key='web series')

# send a message to exchange and exchange will send the message to required queues

channel.basic_publish(exchange='Nikitha_talkz', routing_key='movies',body='I like pspk movies')

# after completing the operation please close the connection

channel.close()