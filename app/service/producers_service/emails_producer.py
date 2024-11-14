import json
import os
from dotenv import load_dotenv
from kafka import KafkaProducer


load_dotenv(verbose=True)


def produce_email(email: dict):
    producer = KafkaProducer(
        bootstrap_servers =os.environ['BOOTSTRAP_SERVERS'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    producer.send(
        'messages.all',
        value=email,
        key=email['email'].encode('utf-8')
    )