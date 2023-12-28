from kafka import KafkaProducer
from time import sleep
import json
import requests


class KafkaDataProducer():
    def __init__(self, bootstrap_servers):
        self.bootstrap_servers = bootstrap_servers

    def produce(self, topic, message):
        try:
            producer = KafkaProducer(bootstrap_servers=self.bootstrap_servers,
                                     value_serializer=lambda x: json.dumps(x).encode('utf-8'))
            producer.send(topic, message)
            producer.flush()
            producer.close()
        except Exception as e:
            print(e)


if __name__ == "__main__":

    bootstrap_servers = "data_analytics_crypto_kafka_kafka_1:9092"
    topic = "crypto_topic"
    message = ["Hello World_", "Hello World_", "Hello World_",
               "Hello World_", "Hello World_", "Hello World_", "Hello World____"]
    for i in message:
        kafka_producer = KafkaDataProducer(bootstrap_servers)
        kafka_producer.produce(topic, i)
