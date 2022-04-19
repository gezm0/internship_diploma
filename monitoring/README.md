# Monitoring

Deploy the Kubernetes dashboard<br>
kubectl apply -f k8s-dashboard.yaml<br>

Create an eks-admin service account and cluster role binding<br>
kubectl apply -f eks-admin-service-account.yaml<br>

Retrieve an authentication token for the eks-admin service account<br>
kubectl -n kube-system describe secret $(kubectl -n kube-system get secret | grep eks-admin | awk '{print $1}')<br>

Start the kubectl proxy<br>
kubectl proxy<br>

Access something like<br>
http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/#!/login
