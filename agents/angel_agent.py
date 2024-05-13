from agents.base_agent import BaseAgent
from models.angel_model import AngelModel
from data.agent_data import load_angel_data
from utils.logger import log

class AngelAgent(BaseAgent):
    def __init__(self, id, name, powers, legion_count=LEGION_COUNT_PER_AGENT):
        super().__init__(id, name)
        self.powers = powers
        self.legion_count = legion_count
        self.legions = []
        self.model = AngelModel()

    def create_legion(self):
        from agents.legion import Legion
        for _ in range(self.legion_count):
            legion = Legion()
            self.legions.append(legion)
            log(event="LegionCreated", message=f"Legion {legion.id} created for Angel {self.id}")

    def call_to_action(self):
        for legion in self.legions:
            legion.deploy()
            log(event="LegionStatus", message=f"Legion {legion.id} deployed by Angel {self.id}")

    def gather_intelligence(self):
        # Placeholder for intelligence gathering logic
        pass

    def report_status(self):
        status = {
            "id": self.id,
            "name": self.name,
            "legion_count": self.legion_count,
            "legions_active": len([l for l in self.legions if l.is_active]),
        }
        log(event="AngelStatus", message=f"Status of Angel {self.id}: {status}")

    @classmethod
    def load_from_data(cls):
        data = load_angel_data()
        angels = []
        for angel_data in data:
            angel = cls(**angel_data)
            angel.create_legion()
            angels.append(angel)
        return angels

    def save_to_model(self):
        self.model.save(self)

    def load_from_model(self):
        angel_data = self.model.load(self.id)
        self.__dict__.update(angel_data)

# Example usage:
# angel_agent = AngelAgent(id=1, name="Michael", powers=["healing", "protection"])
# angel_agent.create_legion()
# angel_agent.call_to_action()
# angel_agent.report_status()