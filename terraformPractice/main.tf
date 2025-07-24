# Simple example of terraform file creation


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









