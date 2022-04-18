output "cluster_host" {
  value = aws_eks_cluster.diploma.endpoint
}

output "kubeconfig_certificate_authority_data" {
  value = aws_eks_cluster.diploma.certificate_authority[0].data
}

output "db_host" {
  value = aws_db_instance.diploma_database.address
}

output "registry_url" {
  value = aws_ecr_repository.diploma.repository_url
}
