# Output Variable

output "public_ip"{
    description = ""
    value = aws_instance.webserver.public_ip
}

