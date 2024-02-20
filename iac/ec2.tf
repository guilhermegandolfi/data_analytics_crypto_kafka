resource "aws_key_pair" "crypto_analytics_aws" {
  key_name   = "crypto-analytics-aws"
  public_key = file("~/crypto-analytics-aws.pub")
}

resource "aws_instance" "example" {
  ami                         = "ami-0c7217cdde317cfec"
  instance_type               = "t2.medium"
  key_name                    = aws_key_pair.crypto_analytics_aws.key_name
  subnet_id                   = aws_subnet.aws_subnet_public.id
  security_groups             = ["${aws_security_group.cyrpto_security_group.id}"]
  tags                        = var.tags
  associate_public_ip_address = true
  user_data                   = <<EOF
#!/bin/bash

git clone https://github.com/guilhermegandolfi/data_analytics_crypto_kafka.git

sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y 

sudo apt install docker-compose -y

PUBLIC_HOSTNAME=$(curl http://169.254.169.254/latest/meta-data/public-hostname)

sed "s/ec2-34-201-154-151.compute-1.amazonaws.com/"$PUBLIC_HOSTNAME"/" data_analytics_crypto_kafka/docker-compose.yml >> data_analytics_crypto_kafka/docker-compose_new.yml 

rm data_analytics_crypto_kafka/docker-compose.yml  

mv data_analytics_crypto_kafka/docker-compose_new.yml data_analytics_crypto_kafka/docker-compose.yml

sudo docker-compose -f data_analytics_crypto_kafka/docker-compose.yml  up -d kafka

sleep 240

sudo docker exec -it data_analytics_crypto_kafka_kafka_1 kafka-topics.sh --bootstrap-server localhost:9092 --topic crypto_topic --create --partitions 3 --replication-factor 1

  EOF
}

