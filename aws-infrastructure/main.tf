terraform {
    required_providers {
        aws = {
            source  = "hashicorp/aws"
            version = "~> 4.5"
        }
    }
    required_version = "~> 1.0"
}

provider "aws" {
    region = "eu-west-2"
    default_tags {
        tags = {
            "Owner"   = "sergei_eremin@epam.com"
            "Project" = "Internship DevOps Diploma"
        }
    }
}

### database ###

resource "aws_db_instance" "diploma_database" {
    identifier             = "diploma-database"
    allocated_storage      = 20
    max_allocated_storage  = 50
    engine                 = "postgres"
    engine_version         = "14.2"
    multi_az               = true
    instance_class         = "db.t3.micro"
    db_name                = var.db_name
    username               = var.db_user
    password               = var.db_password
    vpc_security_group_ids = [ aws_security_group.diploma_database_sg.id ]
    publicly_accessible    = false
    skip_final_snapshot    = true
    tags = {
        "Name" = "Internship DevOps Diploma Database"
        }
}

resource "aws_security_group" "diploma_database_sg" {
    name        = "Database Diploma SG"
    description = "Internship DevOps Diploma Database SG"
    tags = {
        "Name"  = "Diploma DB SG"
    }

    ingress {
        from_port   = "5432"
        to_port     = "5432"
        cidr_blocks = [ "0.0.0.0/0" ]
        protocol    = "tcp"
    }
 
    egress {
        from_port   = 0
        to_port     = 0
        cidr_blocks = [ "0.0.0.0/0" ]
        protocol    = "-1"
        }
}

### cluster ###

resource "aws_eks_cluster" "diploma" {
  name                      = var.cluster_name
  role_arn                  = aws_iam_role.diploma.arn
  enabled_cluster_log_types = ["api", "audit"]

  vpc_config {
    subnet_ids = [ "subnet-046ff1742f5465628", "subnet-02d1738098c3d6a31", "subnet-02b015fc3a4dc6f09" ]
  }

    depends_on = [
    aws_iam_role_policy_attachment.diploma-AmazonEKSClusterPolicy
  ]
}

### cluster role ###

resource "aws_iam_role" "diploma" {
  name = var.cluster_name

  assume_role_policy = <<POLICY
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "eks.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
POLICY
}

resource "aws_iam_role_policy_attachment" "diploma-AmazonEKSClusterPolicy" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"
  role       = aws_iam_role.diploma.name
}

### node group ###

resource "aws_eks_node_group" "diploma" {
  cluster_name    = aws_eks_cluster.diploma.name
  node_group_name = "Diploma_NG"
  node_role_arn   = aws_iam_role.diploma_node_group.arn
  subnet_ids      = [ "subnet-046ff1742f5465628", "subnet-02d1738098c3d6a31", "subnet-02b015fc3a4dc6f09" ]
  instance_types  = [ "t3.small" ]

  scaling_config {
    desired_size = 3
    max_size     = 5
    min_size     = 2
  }

  update_config {
    max_unavailable = 1
  }

  depends_on = [
    aws_iam_role_policy_attachment.diploma-AmazonEKSWorkerNodePolicy,
    aws_iam_role_policy_attachment.diploma-AmazonEKS_CNI_Policy,
    aws_iam_role_policy_attachment.diploma-AmazonEC2ContainerRegistryReadOnly
  ]
}

### node group roles ###

resource "aws_iam_role" "diploma_node_group" {
  name = "eks-node-group-diploma"

  assume_role_policy = jsonencode({
    Statement        = [{
      Action         = "sts:AssumeRole"
      Effect         = "Allow"
      Principal      = {
        Service      = "ec2.amazonaws.com"
      }
    }]
    Version = "2012-10-17"
  })
}

resource "aws_iam_role_policy_attachment" "diploma-AmazonEKSWorkerNodePolicy" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy"
  role       = aws_iam_role.diploma_node_group.name
}

resource "aws_iam_role_policy_attachment" "diploma-AmazonEKS_CNI_Policy" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy"
  role       = aws_iam_role.diploma_node_group.name
}

resource "aws_iam_role_policy_attachment" "diploma-AmazonEC2ContainerRegistryReadOnly" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
  role       = aws_iam_role.diploma_node_group.name
}

### ECR creation ###

#resource "aws_ecr_repository" "diploma" {
#  name                 = var.ecr_repo_name
#  image_tag_mutability = "MUTABLE"
#
# image_scanning_configuration {
#    scan_on_push = true
#  }
#}