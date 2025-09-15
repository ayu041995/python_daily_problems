    variable "ingress_rules" {
    description = "Legacy list of ingress rules"
    type = list(object({
        name     = string
        from     = number
        to       = number
        protocol = string
        cidr     = string
    }))
    default = [
        { name = "http",  from = 80,  to = 80,  protocol = "tcp", cidr = "0.0.0.0/0" },
        { name = "https", from = 443, to = 443, protocol = "tcp", cidr = "0.0.0.0/0" }
    ]
    # http = {
    #     from = 80,  
    #     to = 80,  
    #     protocol = "tcp", 
    #     cidr = "0.0.0.0/0"
    # }
    # https = {
    #     from = 443, 
    #     to = 443, 
    #     protocol = "tcp", 
    #     cidr = "0.0.0.0/0"
    # }
    }
    
    resource "aws_security_group" "web" {
    name        = "inline-q1"
    description = "Example SG"
    vpc_id      = "vpc-PLACEHOLDER"
    for_each = toset(var.ingress_rules.name)
    NAME = each.name
    
    
    #   TODO: Refactor: convert var.ingress_rules to a map keyed by rule name
    #   locals {
    #     ingress_map = { for r in var.ingress_rules : r.name => r }
    #   }
    #   Use for_each on aws_vpc_security_group_ingress_rule with stable keys
    }
    