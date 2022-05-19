#!/bin/bash

cd k8s
kubectl apply -f create_namespaces.yaml
kubectl apply -f metrics-server.yaml
kubectl apply -f horizontalpodautoscaler.yaml
kubectl apply -f autoscaling/cluster-autoscaler-autodiscover.yaml
kubectl apply -f app_secret.yaml
kubectl apply -f app_configmap.yaml
kubectl apply -f app_front_service.yaml
