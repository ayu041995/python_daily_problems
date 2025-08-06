variable "ami_value" {
  type        = string
  default     = "ami-6bfzs8bdvctyf886vsf"
  description = "value of ami"
}

variable "instance_type_value" {
  type        = string
  default     = "t2.micro"
  description = "value of instance_type_value"
}

variable "subnet_id_value" {
  type        = string
  description = "value of subnet_id_value"
}
