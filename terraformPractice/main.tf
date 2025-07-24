# Simple example of terraform file creation
provider "aws"{
    region = "us-east-1"
    profile = "GSC-prod-1"
}

resource "aws_instance" "webserver" {
    ami = "ami_0rfnsbdfvtg87fc7"
    instance_type = "t2.micro"
}

resource "aws_s3_bucket" "finance"{
    bucket = "finance_21096586"
    tags = {
        Description = "finance and payroll"
    }
}

resource "aws_iam_user" "admin_user"{
    name = "Lucky"
    tags = {
        Description = "Team lead"
    }
}

resource "local_file" "pet" {
  sensitive_content = ""
  filename             = "/root/pets.txt"
  file_permission      = 0777
  directory_permission = 0777
  content = "We love pets!"
}

# count and for_each examples

resource "aws_instance" "example"{
    count = 3
    ami = "ami_0rfnsbdfvtg87fc7"
    instance_type = "t2.micro"
}

# Terraform creates 3 EC2 instances: example[0], example[1], example[2].


resource "aws_instance" "example"{
    for_each = toset(["dev","prod","test"])
    ami = "ami_0rfnsbdfvtg87fc7"
    instance_type = "t2.micro"
    tags = {
        Name = each.key
    }
}

# Advanced example

variable "instances" {
  default     = {
    dev = "t2.micro"
    prod = "t2.medium"
  }
  description = "Different instance size for different env"
}

resource "aws_instance" "webserver"{
    for_each = var.instance
    ami = "ami_0rfnsbdfvtg87fc7"
    instance_type = each.value
    tags = {
        Name = each.key
    }
}

# Dynamic blocks in terraform

variable "ingress_port"{
    default = [22,80,443]
}

resource "aws_security_group" "example"{
    name = "example_sg"
    dynamic "ingress"{
        for_each = var.ingress_port
        content{
            from_port = ingress.value
            to_port = ingress.value
            protocol = "tcp"
            cidr_blocks = ["0.0.0.0/0"]
        }
    }
}

# Use a variable to control the number of EC2 instances to create

variable instances {
    default {
        count = 2
    }
}

resource "aws_instance" "webservers" {
    count = var.instances.count
    ami = "ami_0rfnsbdfvtg87fc7"
    instance_type = "m2.xlarge"
    tags = {
        Name = "Webserver-${count.index}"
    }
}


# Create multiple S3 buckets using for_each and a list of names.

variable "nameS3" {
    default = ["dev","prod","stage"]
}

resource "aws_s3_bucket" "my_finance_bucket"{
    for_each = toset(var.nameS3)
    bucket = each.value
}

# output block to display the public IP of an EC2 instance

output "ec2_public_ip" {
    value = aws_instance.webserver.ec2_public_ip
}

# Import an existing EC2 instance into Terraform.

resource "aws_instance" "existing"{

}

# terraform import aws_instance.existing i-0123456789abcdef0











