# Monitoring

Deploy the Kubernetes dashboard
kubectl apply -f k8s-dashboard.yaml

Create an eks-admin service account and cluster role binding
kubectl apply -f eks-admin-service-account.yaml

Retrieve an authentication token for the eks-admin service account
kubectl -n kube-system describe secret $(kubectl -n kube-system get secret | grep eks-admin | awk '{print $1}')

Start the kubectl proxy
kubectl proxy

Access something like
http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/#!/login

Detailed documentation:
https://docs.aws.amazon.com/eks/latest/userguide/dashboard-tutorial.html
