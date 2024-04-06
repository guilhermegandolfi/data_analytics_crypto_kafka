import boto3
from datetime import datetime
import logging


class AmazonS3Connect:

    def __init__(self, bucket):
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s %(levelname)s %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        self.bucket=bucket


    def prefix_partition(self):
        nam_partition = datetime.now()
        nam_partition = nam_partition.strftime('year=%Y/month=%m/day=%d')
        return nam_partition

    def upload_file(self, nam_file, prefix):
        try:
            logging.info(f"upload file {nam_file} to bucket: {self.bucket}")
            nam_file = nam_file.replace("/tmp/", "")
            s3 = boto3.client('s3')
            s3.upload_file(nam_file, self.bucket, f"raw_data/{prefix}/{self.prefix_partition()}/{nam_file}")
            logging.info(f"upload file completed")
        except Exception as e:
            logging.error(e)

if __name__ == "__main__":

    bucket = "crypto-analytics-dev"
    upload = AmazonS3Connect(bucket)
    upload.upload_file('crypto_topic_20240406_003126.json','crypto_topic')
