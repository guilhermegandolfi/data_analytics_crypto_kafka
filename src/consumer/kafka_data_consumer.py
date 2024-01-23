from kafka import KafkaConsumer
from time import sleep
import json
import requests


class KafkaDataConsumer:
    def __init__(self, bootstrap_servers):
        self.bootstrap_servers = bootstrap_servers

    def consumer(self, topic):
        try:
            consumer = KafkaConsumer(
                topic, bootstrap_servers=self.bootstrap_servers, auto_offset_reset='earliest',group_id='my-group2', consumer_timeout_ms=20000)

            for message in consumer:

                print(message.value)
                consumer.commit()

            consumer.close()

        except Exception as e:
            print(e)


if __name__ == "__main__":

    bootstrap_servers = "data_analytics_crypto_kafka_kafka_1:9092"
    topic = "crypto_topic"
    kafka_consumer = KafkaDataConsumer(bootstrap_servers)
    kafka_consumer.consumer(topic)
