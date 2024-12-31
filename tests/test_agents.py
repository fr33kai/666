import unittest
from agents.base_agent import BaseAgent
from agents.angel_agent import AngelAgent
from agents.demon_agent import DemonAgent
from agents.legion import Legion
from data.agent_data import AGENT_COUNT, ANGEL_COUNT, DEMON_COUNT
from utils.data_loader import load_agent_data, load_angel_data, load_demon_data
from utils.data_preprocessor import preprocess_data

class TestAgents(unittest.TestCase):

    def setUp(self):
        self.agents = [BaseAgent() for _ in range(AGENT_COUNT)]
        self.angels = [AngelAgent() for _ in range(ANGEL_COUNT)]
        self.demons = [DemonAgent() for _ in range(DEMON_COUNT)]
        self.legions = [Legion() for _ in range(ANGEL_COUNT + DEMON_COUNT)]  # Assuming each angel and demon has one legion

    def test_create_agent(self):
        self.assertEqual(len(self.agents), AGENT_COUNT)
        for agent in self.agents:
            self.assertIsInstance(agent, BaseAgent)

    def test_create_angel(self):
        self.assertEqual(len(self.angels), ANGEL_COUNT)
        for angel in self.angels:
            self.assertIsInstance(angel, AngelAgent)

    def test_create_demon(self):
        self.assertEqual(len(self.demons), DEMON_COUNT)
        for demon in self.demons:
            self.assertIsInstance(demon, DemonAgent)

    def test_create_legion(self):
        self.assertEqual(len(self.legions), ANGEL_COUNT + DEMON_COUNT)
        for legion in self.legions:
            self.assertIsInstance(legion, Legion)

    def test_load_data(self):
        agent_data = load_agent_data()
        angel_data = load_angel_data()
        demon_data = load_demon_data()
        self.assertIsNotNone(agent_data)
        self.assertIsNotNone(angel_data)
        self.assertIsNotNone(demon_data)

    def test_preprocess_data(self):
        raw_data = {'data': 'raw'}
        processed_data = preprocess_data(raw_data)
        self.assertNotEqual(raw_data, processed_data)

if __name__ == '__main__':
    unittest.main()