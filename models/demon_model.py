```python
from dataclasses import dataclass
from typing import List

@dataclass
class DemonModel:
    id: int
    name: str
    power: int
    legion_ids: List[int]

    def summon_legions(self, legion_data):
        """
        Summon the legions associated with this demon.
        """
        legions = []
        for legion_id in self.legion_ids:
            legion = next((legion for legion in legion_data if legion['id'] == legion_id), None)
            if legion:
                legions.append(legion)
        return legions

    def display_info(self):
        """
        Display information about the demon.
        """
        print(f"Demon ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Power: {self.power}")
        print(f"Legions: {self.legion_ids}")

    def increase_power(self, amount):
        """
        Increase the power of the demon.
        """
        self.power += amount

    def decrease_power(self, amount):
        """
        Decrease the power of the demon.
        """
        if self.power - amount < 0:
            print("Power cannot be negative.")
        else:
            self.power -= amount

    def __post_init__(self):
        """
        Post-initialization checks and setup.
        """
        if not isinstance(self.legion_ids, list):
            raise ValueError("legion_ids must be a list of integers.")
        if not all(isinstance(legion_id, int) for legion_id in self.legion_ids):
            raise ValueError("All items in legion_ids must be integers.")
```