resource "aws_key_pair" "crypto_analytics_aws" {
  key_name   = "crypto-analytics-aws"
  public_key = file("~/crypto-analytics-aws.pub")
}

resource "aws_instance" "example" {
  ami                         = "ami-0c7217cdde317cfec"
  instance_type               = "t2.micro"
  key_name                    = aws_key_pair.crypto_analytics_aws.key_name
  subnet_id                   = aws_subnet.aws_subnet_public.id
  security_groups             = ["${aws_security_group.cyrpto_security_group.id}"]
  tags                        = var.tags
  associate_public_ip_address = true
}



