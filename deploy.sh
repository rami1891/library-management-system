#!/bin/bash

# Apply each YAML file manually
kubectl apply -f namespace.yaml
kubectl apply -f mysql-secret.yaml
kubectl apply -f config-map.yaml
kubectl apply -f mysql-storage.yaml
kubectl apply -f mysql-deployment.yaml
kubectl apply -f library-deployment.yaml 
kubectl apply -f hpa.yaml
# Add more lines as needed for additional YAML files

echo "Deployment complete."
