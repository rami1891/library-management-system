#!/bin/bash

kubectl apply -f namespace.yaml
kubectl apply -f mysql-secret.yaml
kubectl apply -f config-map.yaml
kubectl apply -f mysql-storage.yaml
kubectl apply -f mysql-deployment.yaml
kubectl apply -f library-deployment.yaml 
kubectl apply -f hpa.yaml
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

echo "Deployment complete."
