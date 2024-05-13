#!/bin/bash

# Deployment script for the AI agent project with 144 agents, 72 demons, and 72 angels

echo "Starting deployment process..."

# Load shared dependencies
source config.py

# Build Docker images
echo "Building Docker images..."
docker-compose build

# Deploy the agents using Docker
echo "Deploying agents, angels, and demons with Docker..."
docker-compose up -d

# Apply Kubernetes configurations if available
if [ -f deployment/kubernetes.yml ]; then
    echo "Applying Kubernetes configurations..."
    kubectl apply -f deployment/kubernetes.yml
fi

# Check if Helm charts are available for deployment
if [ -d deployment/helm_chart/ ]; then
    echo "Deploying with Helm charts..."
    helm install ai-agent-project deployment/helm_chart/
fi

echo "Deployment process finished."
echo "The AI agent project with agents, angels, and demons is now running."

# Call the script to start the agents
echo "Starting the agents..."
./scripts/start_agents.sh

echo "Deployment successful. The system is now operational."