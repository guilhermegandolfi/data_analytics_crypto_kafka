resource "aws_vpc" "main" {
  cidr_block = "192.168.0.0/16"
  tags       = var.tags
  enable_dns_support = true
  enable_dns_hostnames = true
}

resource "aws_subnet" "aws_subnet_public" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = "192.168.1.0/24"
  tags              = var.tags
  availability_zone = "${var.region}a"
}

resource "aws_subnet" "aws_subnet_private" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = "192.168.2.0/24"
  tags              = var.tags
  availability_zone = "${var.region}a"
}

resource "aws_internet_gateway" "myIgw" {
  vpc_id = aws_vpc.main.id
}

resource "aws_route_table" "PublicRT" {
  vpc_id = aws_vpc.main.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.myIgw.id
  }
}

resource "aws_route_table_association" "PublicRTAssociation" {
  subnet_id      = aws_subnet.aws_subnet_public.id
  route_table_id = aws_route_table.PublicRT.id
}

resource "aws_security_group" "cyrpto_security_group" {
  name   = "cyrpto_security_group"
  vpc_id = aws_vpc.main.id
  tags   = var.tags
}

resource "aws_vpc_security_group_ingress_rule" "cyrpto_security_group_ingress_rule" {
  security_group_id = aws_security_group.cyrpto_security_group.id
  cidr_ipv4         = "186.249.143.160/32"
  from_port         = 22
  ip_protocol       = "tcp"
  to_port           = 22
  tags              = var.tags
}

resource "aws_vpc_security_group_ingress_rule" "cyrpto_security_group_ingress_rule_zookeper" {
  security_group_id = aws_security_group.cyrpto_security_group.id
  cidr_ipv4         = "186.249.143.160/32"
  from_port         = 2181
  ip_protocol       = "tcp"
  to_port           = 2181
  tags              = var.tags
}


resource "aws_vpc_security_group_ingress_rule" "cyrpto_security_group_ingress_rule_kafka" {
  security_group_id = aws_security_group.cyrpto_security_group.id
  cidr_ipv4         = "186.249.143.160/32"
  from_port         = 9092
  ip_protocol       = "tcp"
  to_port           = 9092
  tags              = var.tags
}



resource "aws_vpc_security_group_egress_rule" "allow_all_traffic_ipv4" {
  security_group_id = aws_security_group.cyrpto_security_group.id
  cidr_ipv4         = "0.0.0.0/0"
  ip_protocol       = "-1" # semantically equivalent to all ports
}