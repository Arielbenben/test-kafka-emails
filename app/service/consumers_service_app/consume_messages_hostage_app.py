import json
import os
from dotenv import load_dotenv
from flask import Flask
from kafka import KafkaConsumer
from app.service.hostage_messages_service import insert_hostage_messages_db


load_dotenv(verbose=True)


def consume_messages_hostage():
    consumer = KafkaConsumer(
        'messages.hostage',
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_deserializer=lambda v: json.loads(v.decode('utf-8'))
    )

    for message in consumer:
        try:
            insert_hostage_messages_db(message.value)
            print(f'Received: Key={message.key}, Value={message.value}')
        except Exception as e:
            print(f'Error processing message: {e}')



app = Flask(__name__)


if __name__ == '__main__':
    consume_messages_hostage()
    app.run()