
terraform{
    backend "s3" {
        bucket = "terraform-state-prod"
        key = "netwrok/vpc/terrafoem.tfstate"
        region = "us-east-1"
        dynamodb_table = "terraform-locks" 
        encrypt = true     
    }   
}