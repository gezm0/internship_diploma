# AWS IaC (RDS and EKS) throgh Terraform

Current downside of this solution is Subnets hardcoding.<br>
Because of I consider database username and password as sensitive data, those data transferring as environment variables. In my case they storing in <b><i>secrets</i></b> file in repo but this file added to <b><i>.cvsignore</i></b> to prevent sensitive data leak. Content of this file is something like this (depends on OS):
# for linux (bash)
export TF_VAR_db_user="demo_user"<br>
export TF_VAR_db_password="demo_password"

# for windows (powershell)
$env:TF_VAR_db_user="demo_user"<br>
$env:TF_VAR_db_password="demo_password"<br>
<br>
You can export those data as environment variables or you can type them manually while applying Terraform manifest.

# Need to fix:
- Security groups to prevent possible undesirable access.