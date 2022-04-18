# Kubernetes infrastructure deployment
app_back.yaml manifest for deploying backend job<br>
app_configmap.yaml configmap with db_host (database endpoint)<br>
app_front.yaml manifest for deploying frontend application<br>
create_namespaces.yaml manifest for creating dev/prod namespaces in k8s<br>
db_create.yaml manifest for creating database schema job<br>
db_drop.yaml manifest for deleting database schema job<br>
There is the app_secret.yaml manifest with credentials, but because of security reasons it added to .gitignore.
