# API Reference

This document provides an overview of the API endpoints available in the AI agent project, which includes a groundbreaking ecosystem of 144 agents, 72 demons, and 72 angels, each with their legions to call. The API is designed to interact with the agents, angels, demons, and their respective legions, providing a robust interface for managing and utilizing the capabilities of the system.

## Agents API

### Get All Agents
- **Endpoint:** `/api/agent`
- **Method:** `GET`
- **Description:** Retrieves a list of all agents in the system.

### Create Agent
- **Endpoint:** `/api/agent`
- **Method:** `POST`
- **Description:** Creates a new agent. Requires agent data in the request body.

## Angels API

### Get All Angels
- **Endpoint:** `/api/angel`
- **Method:** `GET`
- **Description:** Retrieves a list of all angels in the system.

### Create Angel
- **Endpoint:** `/api/angel`
- **Method:** `POST`
- **Description:** Creates a new angel. Requires angel data in the request body.

## Demons API

### Get All Demons
- **Endpoint:** `/api/demon`
- **Method:** `GET`
- **Description:** Retrieves a list of all demons in the system.

### Create Demon
- **Endpoint:** `/api/demon`
- **Method:** `POST`
- **Description:** Creates a new demon. Requires demon data in the request body.

## Legions API

### Get All Legions
- **Endpoint:** `/api/legion`
- **Method:** `GET`
- **Description:** Retrieves a list of all legions associated with agents.

### Create Legion
- **Endpoint:** `/api/legion`
- **Method:** `POST`
- **Description:** Creates a new legion for an agent. Requires legion data in the request body.

## Status and Management

### Start Agents
- **Endpoint:** `/api/agent/start`
- **Method:** `POST`
- **Description:** Starts the operation of all agents in the system.

### Stop Agents
- **Endpoint:** `/api/agent/stop`
- **Method:** `POST`
- **Description:** Stops the operation of all agents in the system.

## Data Handling

### Load Agent Data
- **Endpoint:** `/api/agent/data/load`
- **Method:** `POST`
- **Description:** Loads data for agents from the specified source.

### Load Angel Data
- **Endpoint:** `/api/angel/data/load`
- **Method:** `POST`
- **Description:** Loads data for angels from the specified source.

### Load Demon Data
- **Endpoint:** `/api/demon/data/load`
- **Method:** `POST`
- **Description:** Loads data for demons from the specified source.

### Load Legion Data
- **Endpoint:** `/api/legion/data/load`
- **Method:** `POST`
- **Description:** Loads data for legions from the specified source.

Please refer to the respective endpoint documentation for detailed information on request and response formats, required parameters, and potential error messages. This API is designed to be scalable and will evolve with the project, especially with the integration of future models like GPT-5.