import json
import os
from dotenv import load_dotenv
from flask import Flask
from kafka import KafkaConsumer
from app.repository.mongodb_repository.sentences_repository import insert_email_to_db


load_dotenv(verbose=True)


def consume_email():
    consumer = KafkaConsumer(
        'messages.all',
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_deserializer=lambda v: json.loads(v.decode('utf-8'))
    )

    for message in consumer:
        try:
            insert_email_to_db(message.value)
            print(f'Received: Key={message.key}, Value={message.value}')
        except Exception as e:
            print(f'Error processing message: {e}')



app = Flask(__name__)


if __name__ == '__main__':
    consume_email()
    app.run()