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

### network part ###

resource "aws_vpc" "cluster-vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
        "Name" = "Internship DevOps Diploma VPC"
        }
}

resource "aws_subnet" "pub-subnet-2a" {
  vpc_id                  = aws_vpc.cluster-vpc.id
  cidr_block              = "10.0.100.0/24"
  map_public_ip_on_launch = true
  availability_zone       = "eu-west-2a"
  depends_on              = [ aws_vpc.cluster-vpc ]
    tags = {
        "Name" = "Internship DevOps Diploma Pub Subnet"
        }
}

resource "aws_subnet" "pub-subnet-2b" {
  vpc_id                  = aws_vpc.cluster-vpc.id
  cidr_block              = "10.0.101.0/24"
  map_public_ip_on_launch = true
  availability_zone       = "eu-west-2b"
  depends_on              = [ aws_vpc.cluster-vpc ]
    tags = {
        "Name" = "Internship DevOps Diploma Pub Subnet"
        }
}

resource "aws_subnet" "priv-subnet-2a" {
  vpc_id            = aws_vpc.cluster-vpc.id
  cidr_block        = "10.0.0.0/24"
  availability_zone = "eu-west-2a"
  depends_on        = [ aws_vpc.cluster-vpc ]
    tags = {
        "Name" = "Internship DevOps Diploma Subnets"
        }
}

resource "aws_subnet" "priv-subnet-2b" {
  vpc_id            = aws_vpc.cluster-vpc.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = "eu-west-2b"
  depends_on        = [ aws_vpc.cluster-vpc ]
    tags = {
        "Name" = "Internship DevOps Diploma Subnets"
        }
}

resource "aws_subnet" "priv-subnet-2c" {
  vpc_id            = aws_vpc.cluster-vpc.id
  cidr_block        = "10.0.2.0/24"
  availability_zone = "eu-west-2c"
  depends_on        = [ aws_vpc.cluster-vpc ]
    tags = {
        "Name" = "Internship DevOps Diploma Subnets"
        }
}

resource "aws_internet_gateway" "cluster-igw" {
  vpc_id     = aws_vpc.cluster-vpc.id
  depends_on = [ aws_vpc.cluster-vpc ]
    tags = {
        "Name" = "Internship DevOps Diploma IGW"
        }
}

resource "aws_route_table" "iwg-rou-table" {
  vpc_id     = aws_vpc.cluster-vpc.id
  depends_on = [ aws_vpc.cluster-vpc, aws_internet_gateway.cluster-igw ]
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.cluster-igw.id
  }
    tags = {
        "Name" = "Internship DevOps Diploma Pub Routing"
        }
}

resource "aws_route_table_association" "rou-pub-subnet" {
  subnet_id      = aws_subnet.pub-subnet-2a.id
  route_table_id = aws_route_table.iwg-rou-table.id
  depends_on     = [ aws_subnet.pub-subnet-2a, aws_route_table.iwg-rou-table ]
}

resource "aws_route_table_association" "rou-pub-subnet1" {
  subnet_id      = aws_subnet.pub-subnet-2b.id
  route_table_id = aws_route_table.iwg-rou-table.id
  depends_on     = [ aws_subnet.pub-subnet-2b, aws_route_table.iwg-rou-table ]
}

resource "aws_eip" "nat-ip" {
  vpc = true
    tags = {
        "Name" = "Internship DevOps Diploma EIP for NAT"
        }
}

resource "aws_eip" "nat-ip1" {
  vpc = true
    tags = {
        "Name" = "Internship DevOps Diploma EIP for NAT"
        }
}

resource "aws_nat_gateway" "nat-gateway" {
  allocation_id = aws_eip.nat-ip.id
  subnet_id     = aws_subnet.pub-subnet-2a.id
  depends_on    = [ aws_subnet.pub-subnet-2a, aws_eip.nat-ip ]
    tags = {
        "Name" = "Internship DevOps Diploma NAT GW"
        }
}

resource "aws_nat_gateway" "nat-gateway1" {
  allocation_id = aws_eip.nat-ip1.id
  subnet_id     = aws_subnet.pub-subnet-2b.id
  depends_on    = [ aws_subnet.pub-subnet-2b, aws_eip.nat-ip1 ]
    tags = {
        "Name" = "Internship DevOps Diploma NAT GW"
        }
}

resource "aws_route_table" "nat-route-table" {
  vpc_id     = aws_vpc.cluster-vpc.id
  depends_on = [ aws_vpc.cluster-vpc, aws_nat_gateway.nat-gateway ]
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_nat_gateway.nat-gateway.id
    }
    tags = {
        "Name" = "Internship DevOps Diploma NAT Route Table"
        }
}

resource "aws_route_table" "nat-route-table1" {
  vpc_id     = aws_vpc.cluster-vpc.id
  depends_on = [ aws_vpc.cluster-vpc, aws_nat_gateway.nat-gateway1 ]
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_nat_gateway.nat-gateway1.id
    }
    tags = {
        "Name" = "Internship DevOps Diploma NAT Route Table"
        }
}

resource "aws_route_table_association" "rou-priv-subnet-2a" {
  subnet_id      = aws_subnet.priv-subnet-2a.id
  route_table_id = aws_route_table.nat-route-table.id  
  depends_on     = [ aws_subnet.priv-subnet-2a, aws_route_table.nat-route-table ]
}

resource "aws_route_table_association" "rou-priv-subnet-2b" {
  subnet_id      = aws_subnet.priv-subnet-2b.id
  route_table_id = aws_route_table.nat-route-table.id  
  depends_on     = [ aws_subnet.priv-subnet-2b, aws_route_table.nat-route-table ]
}

resource "aws_route_table_association" "rou-priv-subnet-2c" {
  subnet_id      = aws_subnet.priv-subnet-2c.id
  route_table_id = aws_route_table.nat-route-table1.id  
  depends_on     = [ aws_subnet.priv-subnet-2c, aws_route_table.nat-route-table1 ]
}

### databases ###

resource "aws_db_instance" "diploma_database_dev" {
    identifier             = "diploma-database-dev"
    db_subnet_group_name   = aws_db_subnet_group.diploma_database_group.id
    allocated_storage      = 20
    max_allocated_storage  = 50
    engine                 = "postgres"
    engine_version         = "14.2"
    multi_az               = true
    instance_class         = "db.t3.small"
    db_name                = var.db_name
    username               = var.db_user
    password               = var.db_password
    vpc_security_group_ids = [ aws_security_group.diploma_database_sg.id ]
    publicly_accessible    = false
    skip_final_snapshot    = true
    tags = {
        "Name" = "Internship DevOps Diploma DEV Database"
        }
}

resource "aws_db_instance" "diploma_database_prod" {
    identifier             = "diploma-database-prod"
    db_subnet_group_name   = aws_db_subnet_group.diploma_database_group.id
    allocated_storage      = 20
    max_allocated_storage  = 50
    engine                 = "postgres"
    engine_version         = "14.2"
    multi_az               = true
    instance_class         = "db.t3.small"
    db_name                = var.db_name
    username               = var.db_user
    password               = var.db_password
    vpc_security_group_ids = [ aws_security_group.diploma_database_sg.id ]
    publicly_accessible    = false
    skip_final_snapshot    = true
    tags = {
        "Name" = "Internship DevOps Diploma PROD Database"
        }
}

resource "aws_db_subnet_group" "diploma_database_group" {
    name = "diploma-database-group"
    subnet_ids = [ aws_subnet.priv-subnet-2a.id, aws_subnet.priv-subnet-2b.id, aws_subnet.priv-subnet-2c.id ]
    tags = {
        "Name"  = "Diploma DB Subnets Group"
    }
}

resource "aws_security_group" "diploma_database_sg" {
    name        = "Database Diploma SG"
    vpc_id      = aws_vpc.cluster-vpc.id
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
    subnet_ids = [ aws_subnet.priv-subnet-2a.id, aws_subnet.priv-subnet-2b.id, aws_subnet.priv-subnet-2c.id ]
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
  subnet_ids      = [ aws_subnet.priv-subnet-2a.id, aws_subnet.priv-subnet-2b.id, aws_subnet.priv-subnet-2c.id ]
  instance_types  = [ "t3.small" ]

  tags = {
        "k8s.io/cluster-autoscaler/${var.cluster_name}" = "owned"
        "k8s.io/cluster-autoscaler/enabled" = "true"
        }

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
    aws_iam_role_policy_attachment.diploma-AmazonEKSClusterAutoscalerPolicy,
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

resource "aws_iam_role_policy_attachment" "diploma-AmazonEKSClusterAutoscalerPolicy" {
  policy_arn = "arn:aws:iam::422613489304:policy/k8s-asg-policy"
  role       = aws_iam_role.diploma_node_group.name
}