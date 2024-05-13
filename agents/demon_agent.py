from agents.base_agent import BaseAgent
from agents.legion import Legion
from data.demon_data import DEMON_DATA
from utils.logger import log_event

class DemonAgent(BaseAgent):
    def __init__(self, name, power, legion_count=LEGION_COUNT_PER_AGENT):
        super().__init__(name, power)
        self.legions = [Legion(f"{name}_Legion_{i+1}") for i in range(legion_count)]
        self.type = 'Demon'

    def summon_legions(self):
        for legion in self.legions:
            legion.summon()
            log_event(f"Legion {legion.name} summoned by {self.name}")

    def banish_legions(self):
        for legion in self.legions:
            legion.banish()
            log_event(f"Legion {legion.name} banished by {self.name}")

    def report_status(self):
        status = {
            'name': self.name,
            'power': self.power,
            'type': self.type,
            'legions': [legion.name for legion in self.legions]
        }
        log_event(f"DemonStatus: {status}")
        return status

    @staticmethod
    def create_demons():
        demons = []
        for demon_data in DEMON_DATA:
            demon = DemonAgent(demon_data['name'], demon_data['power'])
            demons.append(demon)
            log_event(f"DemonCreated: {demon.name}")
        return demons

# Example usage:
# demons = DemonAgent.create_demons()
# for demon in demons:
#     demon.summon_legions()
#     demon.report_status()