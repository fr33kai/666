# Installation Guide

Welcome to the installation guide for our groundbreaking AI agent project. This guide will walk you through the steps required to set up and run the project, which includes a diverse ecosystem of 144 agents, 72 angels, and 72 demons, each with their own legions.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package installer)
- Docker (for containerization)
- Kubernetes or Helm (for orchestration, optional)

## Step 1: Clone the Repository

To get started, clone the project repository to your local machine:

```
git clone https://github.com/your-repository/ai-agent-framework.git
cd ai-agent-framework
```

## Step 2: Install Dependencies

Install the required Python packages using pip:

```
pip install -r requirements.txt
```

## Step 3: Set Up the Database

Configure your database by setting the `DATABASE_URI` in the `config.py` file. The project supports various databases, ensure you have the correct driver installed for your chosen database.

## Step 4: Initialize the Application

Run the following command to initialize the application, which will set up the necessary data structures and populate the database with initial data:

```
python main.py --init
```

## Step 5: Start the Agents

To start the agents, angels, and demons, use the provided script:

```
sh scripts/start_agents.sh
```

## Step 6: Verify Installation

To verify that the agents are running correctly, navigate to:

```
http://localhost:5000/
```

You should see the web interface with lists of agents, angels, demons, and legions.

## Optional: Containerization and Orchestration

If you prefer to run the application in a containerized environment, you can build the Docker image using:

```
docker build -t ai-agent-framework .
```

And run the container with:

```
docker-compose up
```

For orchestration with Kubernetes, apply the configuration file:

```
kubectl apply -f deployment/kubernetes.yml
```

Or use the provided Helm chart:

```
helm install ai-agent-framework deployment/helm_chart/
```

## Troubleshooting

If you encounter any issues during installation, please refer to the `docs/troubleshooting_guide.md` for common problems and solutions.

## Conclusion

You have now successfully installed the AI agent project. Explore the capabilities of the agents, angels, demons, and their legions as you delve into this unique and scalable ecosystem.