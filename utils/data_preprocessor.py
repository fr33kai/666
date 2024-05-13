```python
import json
from data.agent_data import AgentSchema
from data.angel_data.json import AngelSchema
from data.demon_data.json import DemonSchema
from data.legion_data.json import LegionSchema

def preprocess_data(data, schema):
    """
    Preprocess the given data according to the specified schema.
    This function ensures that the data conforms to the schema and
    performs any necessary transformations or normalization.

    :param data: The data to preprocess.
    :param schema: The schema to validate the data against.
    :return: Preprocessed data.
    """
    # Validate and clean the data according to the schema
    try:
        validated_data = schema.load(data)
    except Exception as e:
        raise ValueError(f"Data validation error: {e}")

    # Perform additional preprocessing steps if necessary
    # For example, converting strings to datetime objects, normalizing text, etc.

    return validated_data

def preprocess_agent_data(data):
    """
    Preprocess agent data using the AgentSchema.

    :param data: The agent data to preprocess.
    :return: Preprocessed agent data.
    """
    return preprocess_data(data, AgentSchema())

def preprocess_angel_data(data):
    """
    Preprocess angel data using the AngelSchema.

    :param data: The angel data to preprocess.
    :return: Preprocessed angel data.
    """
    return preprocess_data(data, AngelSchema())

def preprocess_demon_data(data):
    """
    Preprocess demon data using the DemonSchema.

    :param data: The demon data to preprocess.
    :return: Preprocessed demon data.
    """
    return preprocess_data(data, DemonSchema())

def preprocess_legion_data(data):
    """
    Preprocess legion data using the LegionSchema.

    :param data: The legion data to preprocess.
    :return: Preprocessed legion data.
    """
    return preprocess_data(data, LegionSchema())
```