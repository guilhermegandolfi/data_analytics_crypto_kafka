variable "project" {
  type    = string
  default = "crypto-analytics"
}

variable "tags" {
  type = map(any)
  default = {
    "Project" = "crypto-analytics"
    "Owner"   = "Guilherme Gandolfi"
  }
}

variable "env" {

}

variable "enviorment" {
  type = map(any)
  default = {
    "dev"  = "dev"
    "prod" = "prod"
  }
}

variable "region" {
  type    = string
  default = "us-east-1"
}