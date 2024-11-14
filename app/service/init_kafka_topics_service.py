import os
from dotenv import load_dotenv
from kafka import KafkaAdminClient
from kafka.admin import NewTopic
from kafka.errors import TopicAlreadyExistsError


load_dotenv(verbose=True)


def init_topics():
    client = KafkaAdminClient(bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'])
    new_member_topic = NewTopic(
        name='messages.all',
        num_partitions=int(os.environ['NUM_PARTITIONS']),
        replication_factor=int(os.environ['NUM_REPLICATION'])
    )
    messages_hostage_topic = NewTopic(
        name='messages.hostage',
        num_partitions=int(os.environ['NUM_PARTITIONS']),
        replication_factor=int(os.environ['NUM_REPLICATION'])
    )
    messages_explosive_topic = NewTopic(
        name='messages.explosive',
        num_partitions=int(os.environ['NUM_PARTITIONS']),
        replication_factor=int(os.environ['NUM_REPLICATION'])
    )

    try:
        client.create_topics([new_member_topic, messages_hostage_topic, messages_explosive_topic])
        print('Topics created successfully')
    except TopicAlreadyExistsError as e:
        print(str(e))
    finally:
        client.close()
