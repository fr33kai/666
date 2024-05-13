# User Guide

Welcome to the user guide for our groundbreaking AI agent project. This document will guide you through the process of interacting with our ecosystem of 144 agents, consisting of 72 angels and 72 demons, each with their own legions to call upon. Our project is designed to be scalable and adaptable, ready to evolve with advancements such as the integration of GPT-5 models.

## Getting Started

To begin using our AI agents, ensure that you have cloned the repository and installed all necessary dependencies listed in `requirements.txt`.

```bash
git clone https://your-repository-url.git
cd your-project-directory
pip install -r requirements.txt
```

## Starting the Agents

To start the agents, you can use the script provided in the `scripts/` directory:

```bash
sh scripts/start_agents.sh
```

This will initialize all agents, angels, demons, and their legions as per the configurations set in `config.py`.

## Interacting with Agents

### Viewing Agent Lists

To view the list of agents, navigate to the web interface and click on the `#agent-list` DOM element. Similarly, you can view angels and demons by clicking on `#angel-list` and `#demon-list`, respectively.

### Starting and Stopping Agents

You can start or stop all agents using the web interface buttons linked to `#start-agents-button` and `#stop-agents-button`. These buttons will trigger the `start_agents()` and `stop_agents()` functions, which manage the agents' activities.

### Using the API

Our project provides a RESTful API for programmatic interaction with the agents. You can create, retrieve, update, and delete agent data using the following endpoints:

- Create an agent: `POST /api/agent`
- Retrieve agent details: `GET /api/agent/{id}`
- Update an agent: `PUT /api/agent/{id}`
- Delete an agent: `DELETE /api/agent/{id}`

The same pattern applies to angels, demons, and legions with their respective endpoints: `/api/angel`, `/api/demon`, and `/api/legion`.

## Data Management

### Loading Data

To load data for agents, angels, demons, and legions, use the `load_agent_data()`, `load_angel_data()`, `load_demon_data()`, and `load_legion_data()` functions, respectively. These functions will fetch data from the corresponding JSON files in the `data/` directory.

### Preprocessing Data

Before using the data, it may need to be preprocessed. Call the `preprocess_data()` function from the `utils/data_preprocessor.py` module to perform any necessary preprocessing steps.

## Logging Events

To log any events or actions, use the `log_event()` function from the `utils/logger.py` module. This will help in maintaining a clear audit trail and debugging if needed.

## Deploying Agents

For deployment, use the provided scripts:

```bash
sh scripts/deploy.sh
sh scripts/undeploy.sh
```

These scripts will help you deploy or undeploy the agents to a server or a containerized environment using Docker and Kubernetes configurations found in `Dockerfile`, `docker-compose.yml`, and `deployment/kubernetes.yml`.

## Conclusion

This user guide provides a basic overview of how to interact with our AI agent ecosystem. For more detailed information, please refer to the other documentation files such as `installation_guide.md`, `api_reference.md`, and `development_guide.md`. Enjoy exploring the capabilities of our unique and scalable AI agents!