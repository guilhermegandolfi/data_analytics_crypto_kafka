FROM ubuntu

WORKDIR /app

RUN apt-get update && apt install -y curl  && apt install -y default-jre

RUN curl https://dlcdn.apache.org/kafka/3.6.1/kafka_2.13-3.6.1.tgz -o kafka_2.tgz

RUN tar -xzf kafka_2.tgz

ENTRYPOINT ["kafka_2.13-3.6.1/bin/kafka-server-start.sh", "kafka_2.13-3.6.1/config/server.properties"]


