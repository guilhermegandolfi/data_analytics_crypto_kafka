from amazon_s3_conect import AmazonS3Connect
from kafka_data_consumer import KafkaDataConsumer
import logging
import os

def lambda_handler(event, lambda_context):
    logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s %(levelname)s %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    try:
        logging.info('Started consuemr of kafka')
        nam_kafka_broker = os.environ['NAM_KAFKA_BROKER']
        nam_topic = os.environ['NAM_TOPIC']
        bootstrap_servers = f"{nam_kafka_broker}:9092"
        kafka_consumer = KafkaDataConsumer(bootstrap_servers)
        nam_file = kafka_consumer.consumer(nam_topic)
        
        nam_bucket = os.environ['NAM_BUCKET']
        logging.info(f'Started wirte file to bucket:{nam_bucket}') 
        s3_import = AmazonS3Connect(nam_bucket)
        nam_prefix = f"{nam_topic}"
        s3_import.upload_file(nam_file, nam_prefix)

    except Exception as e:
        logging.error(e)
