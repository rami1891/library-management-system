#!/bin/bash

# Variables
NAMESPACE="kube-system"
DEPLOYMENT_NAME="metrics-server"
METRICS_SERVER_IMAGE="k8s.gcr.io/metrics-server/metrics-server:v0.6.3"
KUBECTL="kubectl"

# Function to update metrics-server deployment
update_metrics_server() {
    echo "Updating metrics-server deployment to use --kubelet-insecure-tls..."
    $KUBECTL patch deployment $DEPLOYMENT_NAME -n $NAMESPACE --type='json' -p='[{"op": "add", "path": "/spec/template/spec/containers/0/args/-", "value": "--kubelet-insecure-tls"}]'
}




# Main script execution
echo "Starting troubleshooting for metrics-server..."

update_metrics_server
sleep 10 # Wait for the update to take effect


# Uncomment if you're using Minikube and need to restart it
# restart_minikube

echo "Metrics-server troubleshooting complete."
