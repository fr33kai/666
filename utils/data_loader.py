```python
import json
from data.agent_data import AGENT_COUNT, DEMON_COUNT, ANGEL_COUNT

def load_data(file_path):
    """
    Load data from a JSON file and return the data.
    :param file_path: str, the path to the data file.
    :return: dict, the data loaded from the file.
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def load_agent_data():
    """
    Load agent data from the predefined JSON file.
    :return: dict, the data of all agents.
    """
    return load_data('data/agent_data.json')

def load_angel_data():
    """
    Load angel data from the predefined JSON file.
    :return: dict, the data of all angels.
    """
    return load_data('data/angel_data.json')

def load_demon_data():
    """
    Load demon data from the predefined JSON file.
    :return: dict, the data of all demons.
    """
    return load_data('data/demon_data.json')

def load_legion_data():
    """
    Load legion data from the predefined JSON file.
    :return: dict, the data of all legions.
    """
    return load_data('data/legion_data.json')

def validate_data_counts():
    """
    Validate that the loaded data matches the expected counts of agents, demons, and angels.
    :return: bool, True if the data counts are correct, False otherwise.
    """
    agents = load_agent_data()
    angels = load_angel_data()
    demons = load_demon_data()

    return len(agents) == AGENT_COUNT and len(angels) == ANGEL_COUNT and len(demons) == DEMON_COUNT
```