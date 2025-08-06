resource "aws_instance" "example1"{
    ami = var.ami_value
    instance_type = var.instance_type_value
    subnet_id = var.subnet_id_value
}

# Backend bucket and dynamoDB configuration

resource "aws_s3_bucket" "s3_bucket"{
    bucket_name = "ayushi-s3-backend-xyz"
}

resource "aws_dynamodb_table"{
    name = "terraform_lock"
    billing = "PAY_PER_REQUEST"
    hash_key = "LockID"

    attribute{
        name = "LockID"
        type = "S"
    }
}