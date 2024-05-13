from flask import Flask, render_template, jsonify, request
from agents.manager import AgentManager
from data.agent_data import AGENT_COUNT, ANGEL_COUNT, DEMON_COUNT
from utils.logger import log_event

app = Flask(__name__)

# Initialize the Agent Manager
agent_manager = AgentManager(AGENT_COUNT, ANGEL_COUNT, DEMON_COUNT)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/agent', methods=['GET', 'POST'])
def agent_api():
    if request.method == 'POST':
        agent_manager.create_agent()
        log_event('AgentCreated')
        return jsonify({'status': 'Agent created'}), 201
    else:
        agents = agent_manager.get_agents()
        return jsonify(agents)

@app.route('/api/angel', methods=['GET', 'POST'])
def angel_api():
    if request.method == 'POST':
        agent_manager.create_angel()
        log_event('AngelCreated')
        return jsonify({'status': 'Angel created'}), 201
    else:
        angels = agent_manager.get_angels()
        return jsonify(angels)

@app.route('/api/demon', methods=['GET', 'POST'])
def demon_api():
    if request.method == 'POST':
        agent_manager.create_demon()
        log_event('DemonCreated')
        return jsonify({'status': 'Demon created'}), 201
    else:
        demons = agent_manager.get_demons()
        return jsonify(demons)

@app.route('/api/legion', methods=['GET', 'POST'])
def legion_api():
    if request.method == 'POST':
        agent_id = request.json.get('agent_id')
        legion = agent_manager.create_legion(agent_id)
        log_event('LegionCreated')
        return jsonify({'status': 'Legion created', 'legion': legion}), 201
    else:
        legions = agent_manager.get_legions()
        return jsonify(legions)

@app.route('/start-agents', methods=['POST'])
def start_agents():
    agent_manager.start_agents()
    log_event('AgentStatus', 'All agents started')
    return jsonify({'status': 'All agents started'}), 200

@app.route('/stop-agents', methods=['POST'])
def stop_agents():
    agent_manager.stop_agents()
    log_event('AgentStatus', 'All agents stopped')
    return jsonify({'status': 'All agents stopped'}), 200

if __name__ == '__main__':
    app.run(debug=True)