from kafka_data_producer import KafkaDataProducer
from api_client import APIClient


class Main:

    def main():
        try:
            url = "https://api.blockchain.com/v3/exchange/tickers"
            api_client = APIClient(url)
            response = api_client.get_request()
            kafka_producer = KafkaDataProducer("data_analytics_crypto_kafka_kafka_1:9092")
            kafka_producer.producer("crypto_topic", response)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    Main.main()
