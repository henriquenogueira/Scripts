variable "aws_access_key" {}
variable "aws_secret_key" {}

provider "aws" {
  region     = "us-east-1"
  access_key = var.aws_access_key
  secret_key = var.aws_secret_key
}
resource "aws_instance" "elk" {
  ami           = "ami-09d8b5222f2b93bf0"
  instance_type = "t3a.small"
  key_name = "Henrique"
  subnet_id = "subnet-050109879a87f511d"
  security_groups = ["sg-0cf50f6ebf44e1830"]

  tags = {
    Name = "lab" 
    Platform = "AWS LINUX2"     
    Project = "LOGS"    
    Service = "teste"     
    VPC-Name = "VPC_DEFAULT"
  }
  volume_tags = {
    Name = "lab" 
    Platform = "AWS LINUX2"     
    Project = "LAB"    
    Service = "LAB"     
    VPC-Name = "teste"      
  }
}
