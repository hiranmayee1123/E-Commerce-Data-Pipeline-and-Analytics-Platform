provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "ecommerce_data" {
  bucket = "ecommerce-data-pipeline"
  acl    = "private"
}

resource "aws_rds_instance" "ecommerce_db" {
  allocated_storage    = 20
  engine              = "postgres"
  instance_class
