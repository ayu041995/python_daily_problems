# backend file

terraform{
    backend "s3" {
        bucket = "terraform-state-prod"
        key = "netwrok/vpc/terrafoem.tfstate"
        region = "us-east-1"
        dynamodb_table = "terraform-locks" 
        encrypt = true     
    }   
}

# Enables locking via DynamoDB.
# Key is used inside a remote backend block, specifically for the S3 backend, and it tells Terraform where in the S3 bucket to store the state file.