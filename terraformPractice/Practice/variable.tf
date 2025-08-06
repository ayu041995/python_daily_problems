variable "instance_type"{
    description = "EC2 instance type"
    type = string
    default = "t2.micro"
}

variable "instances" {
  default     = {
    dev = "t2.micro"
    prod = "t2.medium"
  }
  description = "Different instance size for different env"
}
