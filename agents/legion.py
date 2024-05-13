```python
from agents.base_agent import BaseAgent
from data.legion_data import load_legion_data
from utils.logger import log_event

class Legion:
    def __init__(self, id, name, agents):
        self.id = id
        self.name = name
        self.agents = agents  # List of BaseAgent instances

    def summon(self):
        log_event(f"Legion {self.name} summoned")
        for agent in self.agents:
            agent.activate()

    def dismiss(self):
        log_event(f"Legion {self.name} dismissed")
        for agent in self.agents:
            agent.deactivate()

    def report_status(self):
        statuses = [agent.status() for agent in self.agents]
        log_event(f"Status report for Legion {self.name}: {statuses}")
        return statuses

    @classmethod
    def create_legion(cls, legion_data):
        agents = []
        for agent_data in legion_data['agents']:
            if agent_data['type'] == 'angel':
                from agents.angel_agent import AngelAgent
                agents.append(AngelAgent(**agent_data))
            elif agent_data['type'] == 'demon':
                from agents.demon_agent import DemonAgent
                agents.append(DemonAgent(**agent_data))
            else:
                agents.append(BaseAgent(**agent_data))
        return cls(legion_data['id'], legion_data['name'], agents)

    @staticmethod
    def load_legions():
        legions_data = load_legion_data()
        return [Legion.create_legion(ld) for ld in legions_data]

# Example usage:
# legions = Legion.load_legions()
# for legion in legions:
#     legion.summon()
#     legion.report_status()
#     legion.dismiss()
```