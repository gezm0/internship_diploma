# AWS IaC (RDS and EKS) through Terraform

Current downside of this solution is Subnets hardcoding.<br>
Because of I consider database username and password as sensitive data, those data transferring as environment variables. In my case they storing in <b><i>secrets</i></b> file in repo but this file added to <b><i>.cvsignore</i></b> to prevent sensitive data leak. Content of this file is something like this (depends on OS):
# for linux (bash)
export TF_VAR_db_user="test"<br>
export TF_VAR_db_password="test"<br>
export TF_VAR_db_name="test"<br>
export db_host="localhost"<br>

# for windows (powershell)
$env:TF_VAR_db_user="test"<br>
$env:TF_VAR_db_password="test"<br>
$env:TF_VAR_db_name="test"<br>
$env:db_host="localhost"<br><br>
You can export those data as environment variables or you can type them manually while applying Terraform manifest.

# Need to fix
- <s>Security groups to prevent possible undesirable access.</s> RDS endpoint located inside local subnet and has no access outside as vice versa (checked).

# Current status
- Added AWS EKS cluster with command "aws eks --region eu-west-2 update-kubeconfig --name eks-cluster-diploma". Connected to it and checked cluster status.

![photo_2022-04-12_11-10-21](https://user-images.githubusercontent.com/94368360/162912915-d7efafd3-1b8b-49f0-b3b5-bff39cb35ab1.jpg)

After that deployed simple "helloworld" pod to cluster, logged in to it, installed "ping" and "postgresql-client" in this container. And finally connected to my RDS database with my credentials.

![photo_2022-04-12_11-03-26](https://user-images.githubusercontent.com/94368360/162912501-e0920097-6def-482d-9d2e-096ea2925437.jpg)

- Added ECR and its output for further use (not checked yet).
