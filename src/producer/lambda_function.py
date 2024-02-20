from kafka_data_producer import KafkaDataProducer
from api_client import APIClient
import os
import logging


def lambda_handler(event, lambda_context):
    logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s %(levelname)s %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    try:
        logging.info("Initiated the lambda function ")
        nam_kafka_broker = os.environ['NAM_KAFKA_BROKER']
        nam_topic = os.environ['NAM_TOPIC']
        url = "https://api.blockchain.com/v3/exchange/tickers"
        api_client = APIClient(url)
        response = api_client.get_request()
        kafka_producer = KafkaDataProducer(f"{nam_kafka_broker}:9092")
        kafka_producer.producer(f"{nam_topic}", response)
    except Exception as e:
        logging.error(e)

if __name__ == "__main__":
    os.environ['NAM_KAFKA_BROKER'] = "data_analytics_crypto_kafka_kafka_1"
    os.environ['NAM_TOPIC'] = "crypto-topic"
    lambda_handler(None, None)
