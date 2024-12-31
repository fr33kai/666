from dataclasses import dataclass
from typing import List

@dataclass
class AngelModel:
    id: int
    name: str
    power: str
    legion_count: int = LEGION_COUNT_PER_AGENT
    legions: List[int] = None

    def __post_init__(self):
        if self.legions is None:
            self.legions = []

    def summon_legions(self):
        # Placeholder for legion summoning logic
        pass

    def report_status(self):
        return {
            'id': self.id,
            'name': self.name,
            'power': self.power,
            'legion_count': self.legion_count,
            'legions': self.legions
        }

    def add_legion(self, legion_id):
        if legion_id not in self.legions:
            self.legions.append(legion_id)

    def remove_legion(self, legion_id):
        if legion_id in self.legions:
            self.legions.remove(legion_id)

# Import shared dependencies
from data.agent_data import AngelSchema
from utils.logger import log_event

# Constants
LEGION_COUNT_PER_AGENT = 10  # This should be defined in a shared config file

# Example usage
if __name__ == "__main__":
    # Create an example angel with a unique ID and name
    angel = AngelModel(id=1, name="Michael", power="Protection")
    # Add legions to the angel
    for i in range(angel.legion_count):
        angel.add_legion(i)
    # Log the status of the angel
    log_event("AngelCreated", angel.report_status())