from amazon_s3_conect import AmazonS3Connect
from kafka_data_consumer import KafkaDataConsumer
import logging
import os

def lambda_handler(event, lambda_context):
    try:
        
        bootstrap_servers = "data_analytics_crypto_kafka_kafka_1:9092"
        topic = "crypto-topic"
        kafka_consumer = KafkaDataConsumer(bootstrap_servers)
        nam_file = kafka_consumer.consumer(topic)

        nam_bucket = 'crypto-analytics-dev'
        s3_import = AmazonS3Connect(nam_bucket)
        nam_prefix = f"raw_data/{s3_import.prefix_partition()}"
        s3_import.upload_file(nam_prefix, nam_file)

    except Exception as e:
        logging.error(e)