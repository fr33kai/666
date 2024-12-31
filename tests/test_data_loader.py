import unittest
from utils.data_loader import load_data
from data.agent_data import AGENT_COUNT, DEMON_COUNT, ANGEL_COUNT

class TestDataLoader(unittest.TestCase):

    def test_load_agent_data(self):
        agents = load_data('data/agent_data.py')
        self.assertEqual(len(agents), AGENT_COUNT)

    def test_load_angel_data(self):
        angels = load_data('data/angel_data.json')
        self.assertEqual(len(angels), ANGEL_COUNT)

    def test_load_demon_data(self):
        demons = load_data('data/demon_data.json')
        self.assertEqual(len(demons), DEMON_COUNT)

    def test_load_legion_data(self):
        legions = load_data('data/legion_data.json')
        # Assuming each agent has a legion, the total legions should be equal to AGENT_COUNT
        self.assertEqual(len(legions), AGENT_COUNT)

if __name__ == '__main__':
    unittest.main()