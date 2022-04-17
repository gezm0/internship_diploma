output "endpoint" {
  value = aws_eks_cluster.diploma.endpoint
}

output "kubeconfig-certificate-authority-data" {
  value = aws_eks_cluster.diploma.certificate_authority[0].data
}

output "database-address" {
  value = aws_db_instance.diploma_database.address
}

output "registry-id" {
  value = aws_ecr_repository.diploma.repository_url
}
