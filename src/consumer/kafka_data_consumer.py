from kafka import KafkaConsumer
from time import sleep
import json
from datetime import datetime
import logging


class KafkaDataConsumer:
    def __init__(self, bootstrap_servers):
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s %(levelname)s %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        self.bootstrap_servers = bootstrap_servers


    def load_delta(self):
        nam_date=datetime.now()
        nam_date=nam_date.strftime('%Y%m%d_%H%M%S')
        return nam_date
       
    def consumer(self, topic):
        try:
            logging.info(f"Init of consumer message from kafka topic:{topic}")
            nam_file=f"{topic}_{self.load_delta()}.json"
            consumer = KafkaConsumer(
                topic, bootstrap_servers=self.bootstrap_servers, auto_offset_reset='earliest',group_id='my-group2',
                value_deserializer = lambda x:json.loads(x.decode('utf-8')),consumer_timeout_ms=20000)
            logging.info(f"Creating file to save the message {nam_file}")
            with open(nam_file, "w") as f:
                for message in consumer:
                    json.dump(message.value, f)
                    consumer.commit()

            consumer.close()
            logging.info("Message was consumed")
            return nam_file

        except Exception as e:
            logging.error(e)
            print(e)


if __name__ == "__main__":

    bootstrap_servers = "data_analytics_crypto_kafka_kafka_1:9092"
    topic = "crypto-topic"
    kafka_consumer = KafkaDataConsumer(bootstrap_servers)
    kafka_consumer.consumer(topic)

