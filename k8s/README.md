# Kubernetes infrastructure deployment
<b>app_back.yaml</b> manifest for deploying backend job<br>
<b>app_configmap.yaml</b> configmap with db_host (database endpoint)<br>
<b>app_front.yaml</b> manifest for deploying frontend application<br>
<b>create_namespaces.yaml</b> manifest for creating dev/prod namespaces in k8s<br>
<b>db_create.yaml</b> manifest for creating database schema job<br>
<b>db_drop.yaml</b> manifest for deleting database schema job<br><br>
There is the <b>app_secret.yaml</b> manifest with credentials, but because of security reasons it added to .gitignore.
# How to use it
Set environment variables as <a href="https://github.com/gezm0/internship_diploma/tree/main/aws-infrastructure">here</a>, for example.<br>
Edit <b>app_secret.yaml</b> and <b>app_configmap.yaml</b> with you secrets and variables.<br>
<b>kubectl.exe apply -f app_secret.yaml</b> # create secret in k8s<br>
<b>kubectl.exe apply -f app_configmap.yaml</b> # create configmap in k8s<br>
<b>kubectl.exe apply -f db_create.yaml</b> # job to create database schema<br>
<b>kubectl.exe apply -f app_back.yaml</b> # job to fill database with data<br>
<b>kubectl.exe apply -n dev -f app_front.yaml</b> # deployment to start frontend in namespace <i>dev</i><br><br>
<b>kubectl.exe apply -f db_drop.yaml</b> # if you want run job to drop database<br>
