# Kubernetes infrastructure deployment
<b>app_back.yaml</b> manifest for deploying backend job<br>
<b>app_configmap.yaml</b> configmap with db_host (database endpoint)<br>
<b>app_front.yaml</b> manifest for deploying frontend application<br>
<b>create_namespaces.yaml</b> manifest for creating dev/prod namespaces in k8s<br>
<b>db_create.yaml</b> manifest for creating database schema job<br>
<b>db_drop.yaml</b> manifest for deleting database schema job<br><br>
There is the <b>app_secret.yaml</b> manifest with credentials, but because of security reasons it added to .gitignore.
