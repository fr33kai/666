from agents.manager import AgentManager
from utils.data_loader import load_agent_data, load_angel_data, load_demon_data, load_legion_data
from utils.logger import log_event
from config import AGENT_COUNT, ANGEL_COUNT, DEMON_COUNT, LEGION_COUNT_PER_AGENT

def main():
    try:
        # Initialize the Agent Manager
        agent_manager = AgentManager(AGENT_COUNT, ANGEL_COUNT, DEMON_COUNT, LEGION_COUNT_PER_AGENT)

        # Load data for agents, angels, demons, and legions
        agent_data = load_agent_data('data/agent_data.py')
        angel_data = load_angel_data('data/angel_data.json')
        demon_data = load_demon_data('data/demon_data.json')
        legion_data = load_legion_data('data/legion_data.json')

        # Create agents, angels, demons, and their legions
        agent_manager.create_agents(agent_data)
        agent_manager.create_angels(angel_data)
        agent_manager.create_demons(demon_data)
        agent_manager.create_legions(legion_data)

        # Start the agents
        agent_manager.start_agents()

        # Log the event
        log_event("All agents started successfully.")

    except Exception as e:
        log_event(f"An error occurred: {e}")

if __name__ == "__main__":
    main()