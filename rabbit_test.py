import pika
import logging
logging.basicConfig(level=logging.DEBUG)
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',5672))