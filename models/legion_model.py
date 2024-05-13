```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class LegionModel:
    id: int
    name: str
    allegiance: str  # 'angel' or 'demon'
    members: List[int] = field(default_factory=list)

    def add_member(self, agent_id: int):
        if agent_id not in self.members:
            self.members.append(agent_id)

    def remove_member(self, agent_id: int):
        if agent_id in self.members:
            self.members.remove(agent_id)

    def get_member_count(self) -> int:
        return len(self.members)

    def serialize(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'allegiance': self.allegiance,
            'members': self.members
        }

    @staticmethod
    def deserialize(data: dict):
        return LegionModel(
            id=data['id'],
            name=data['name'],
            allegiance=data['allegiance'],
            members=data.get('members', [])
        )
```