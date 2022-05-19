variable "db_user" {
    description = "RDS user name"
    type        = string
    sensitive   = true
}

variable "db_password" {
    description = "RDS user password"
    type        = string
    sensitive   = true
}

variable "db_name" {
    description = "RDS database name"
    type        = string
    default     = "diploma"
}

variable "cluster_name" {
    description = "EKS cluster name"
    default = "eks-cluster-diploma"
    type    = string
}
