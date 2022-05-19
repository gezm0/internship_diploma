output "cluster_host" {
  value = aws_eks_cluster.diploma.endpoint
}

output "kubeconfig_certificate_authority_data" {
  value = aws_eks_cluster.diploma.certificate_authority[0].data
}

output "db_host_dev" {
  value = aws_db_instance.diploma_database_dev.address
}

output "db_host_prod" {
  value = aws_db_instance.diploma_database_prod.address
}