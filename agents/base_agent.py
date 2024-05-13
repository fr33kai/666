```python
from abc import ABC, abstractmethod
from data.agent_data import AgentSchema
from utils.logger import log

class BaseAgent(ABC):
    def __init__(self, id, name, attributes):
        self.id = id
        self.name = name
        self.attributes = attributes
        self.legions = []

    @abstractmethod
    def act(self):
        pass

    def add_legion(self, legion):
        self.legions.append(legion)
        log(f"Legion {legion.id} added to {self.name}")

    def remove_legion(self, legion):
        self.legions.remove(legion)
        log(f"Legion {legion.id} removed from {self.name}")

    def get_status(self):
        return {
            'id': self.id,
            'name': self.name,
            'attributes': self.attributes,
            'legions': [legion.get_status() for legion in self.legions]
        }

    def serialize(self):
        return AgentSchema().dump(self.get_status())

    def __repr__(self):
        return f"<BaseAgent id={self.id} name={self.name}>"
```