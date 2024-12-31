#!/bin/bash

# Stop all running agents, angels, demons, and their legions
echo "Stopping all agents..."
bash scripts/stop_agents.sh

# Undeploy from Kubernetes
echo "Undeploying from Kubernetes..."
kubectl delete -f deployment/kubernetes.yml

# Remove Helm chart if it was used for deployment
echo "Removing Helm chart..."
helm uninstall my-ai-agent-project

# Optionally, remove Docker containers and images
echo "Removing Docker containers..."
docker-compose -f docker-compose.yml down

echo "Undeployment completed successfully."