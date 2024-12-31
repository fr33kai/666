from flask import Blueprint, jsonify, request
from agents.manager import AgentManager
from utils.logger import log

agent_api_blueprint = Blueprint('agent_api', __name__)
agent_manager = AgentManager()

@agent_api_blueprint.route('/api/agent', methods=['POST'])
def create_agent():
    try:
        data = request.json
        agent = agent_manager.create_agent(data)
        log_event('AgentCreated', agent)
        return jsonify(agent), 201
    except Exception as e:
        log_event('Error', str(e))
        return jsonify({'error': str(e)}), 500

@agent_api_blueprint.route('/api/agent/<int:agent_id>', methods=['GET'])
def get_agent(agent_id):
    try:
        agent = agent_manager.get_agent(agent_id)
        if agent:
            log_event('AgentStatus', agent)
            return jsonify(agent), 200
        else:
            return jsonify({'error': 'Agent not found'}), 404
    except Exception as e:
        log_event('Error', str(e))
        return jsonify({'error': str(e)}), 500

@agent_api_blueprint.route('/api/agent', methods=['GET'])
def list_agents():
    try:
        agents = agent_manager.list_agents()
        log_event('AgentStatus', agents)
        return jsonify(agents), 200
    except Exception as e:
        log_event('Error', str(e))
        return jsonify({'error': str(e)}), 500

@agent_api_blueprint.route('/api/agent/<int:agent_id>', methods=['DELETE'])
def delete_agent(agent_id):
    try:
        result = agent_manager.delete_agent(agent_id)
        log_event('AgentDeleted', {'agent_id': agent_id})
        return jsonify(result), 200
    except Exception as e:
        log_event('Error', str(e))
        return jsonify({'error': str(e)}), 500

@agent_api_blueprint.route('/api/agent/start', methods=['POST'])
def start_agents():
    try:
        agent_manager.start_agents()
        log_event('AgentsStarted', {})
        return jsonify({'message': 'Agents started successfully'}), 200
    except Exception as e:
        log_event('Error', str(e))
        return jsonify({'error': str(e)}), 500

@agent_api_blueprint.route('/api/agent/stop', methods=['POST'])
def stop_agents():
    try:
        agent_manager.stop_agents()
        log_event('AgentsStopped', {})
        return jsonify({'message': 'Agents stopped successfully'}), 200
    except Exception as e:
        log_event('Error', str(e))
        return jsonify({'error': str(e)}), 500
