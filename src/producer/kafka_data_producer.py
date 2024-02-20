from kafka import KafkaProducer
import json
import logging


class KafkaDataProducer():
    def __init__(self, bootstrap_servers):
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s %(levelname)s %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        self.bootstrap_servers = bootstrap_servers

    def producer(self, topic, message):
        try:
            logging.info("Conection with kafka broker")
            producer = KafkaProducer(bootstrap_servers=self.bootstrap_servers,
                                     value_serializer=lambda x: json.dumps(x).encode('utf-8'))
            logging.info(f"Sending a message to topic: {topic}")
            producer.send(topic, message)
            producer.flush()
            producer.close()
            logging.info("Message sent to kafka broker")
        except Exception as e:
            logging.error(e)


if __name__ == "__main__":

    bootstrap_servers = "data_analytics_crypto_kafka_kafka_1:9092"
    topic = "crypto_topic"
    message = ["aaa", "aaa", "Hello World_",
               "Hello World_", "Hello World_", "Hello World_", "Hello World____"]
    
    for i in message:
        kafka_producer = KafkaDataProducer(bootstrap_servers)
        kafka_producer.producer(topic, i)
