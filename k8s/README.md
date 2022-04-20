# Kubernetes infrastructure deployment
<b>app_back.yaml</b> manifest for deploying backend job<br>
<b>app_configmap.yaml</b> configmap with db_host (database endpoint)<br>
<b>app_front.yaml</b> manifest for deploying frontend application<br>
<b>cloud_watch_fluentbit.yaml</b> fluentbit logging implementation<br>
<b>create_namespaces.yaml</b> manifest for creating dev/prod namespaces in k8s<br>
<b>db_create.yaml</b> manifest for creating database schema job<br>
<b>db_drop.yaml</b> manifest for deleting database schema job<br>
<b>metrics-server.yaml</b> manifest for metrics server installation (necessary for HorizontalPodAutoscaler)<br>
<b>horizontalpodautoscaler.yaml</b> manifest for HorizontalPodAutoscaler<br><br>
There is the <b>app_secret.yaml</b> manifest with credentials, but because of security reasons it added to .gitignore.
# How to use it
Set environment variables as <a href="https://github.com/gezm0/internship_diploma/tree/main/aws-infrastructure">here</a>, for example.<br><br>
Edit <b>app_secret.yaml</b> and <b>app_configmap.yaml</b> with you secrets and variables.<br><br>
<b>kubectl apply -f metrics-server.yaml</b> # install metrics server<br>
<b>kubectl apply -f cloud_watch_fluentbit.yaml</b> to deploy fluentbit logging implementation<br>
<b>kubectl apply -f horizontalpodautoscaler.yaml</b> # create HorizontalPodAutoscaler<br>
<b>kubectl apply -f app_secret.yaml</b> # create secret for applications<br>
<b>kubectl apply -f app_configmap.yaml</b> # create configmap for applications<br>
<b>kubectl apply -f db_create.yaml</b> # job to create database schema<br>
<b>kubectl apply -f app_back.yaml</b> # job to fill database with data<br>
<b>kubectl apply -f app_front.yaml</b> # deployment to start frontend<br><br>
<b>kubectl apply -f db_drop.yaml</b> # if you want run job to drop database<br>
