FROM ubuntu

USER root

RUN apt-get update  
RUN apt install -y curl
RUN apt install -y default-jdk

RUN curl https://dlcdn.apache.org/kafka/3.6.1/kafka_2.13-3.6.1.tgz -o kafka_2.tgz

RUN tar -xzf kafka_2.tgz

ENTRYPOINT ["kafka_2.13-3.6.1/bin/zookeeper-server-start.sh", "kafka_2.13-3.6.1/config/zookeeper.properties"]