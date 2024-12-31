import unittest
from utils.data_preprocessor import preprocess
from data.agent_data import AgentSchema
from data.angel_data import AngelSchema
from data.demon_data import DemonSchema
from data.legion_data import LegionSchema

class TestDataPreprocessor(unittest.TestCase):

    def test_preprocess_agent_data(self):
        raw_data = {
            'id': 'agent-001',
            'name': 'Agent One',
            'status': 'active'
        }
        processed_data = preprocess(raw_data, AgentSchema)
        self.assertEqual(processed_data['id'], raw_data['id'])
        self.assertEqual(processed_data['name'], raw_data['name'])
        self.assertEqual(processed_data['status'], raw_data['status'])

    def test_preprocess_angel_data(self):
        raw_data = {
            'id': 'angel-001',
            'name': 'Angel One',
            'power': 'healing'
        }
        processed_data = preprocess(raw_data, AngelSchema)
        self.assertEqual(processed_data['id'], raw_data['id'])
        self.assertEqual(processed_data['name'], raw_data['name'])
        self.assertEqual(processed_data['power'], raw_data['power'])

    def test_preprocess_demon_data(self):
        raw_data = {
            'id': 'demon-001',
            'name': 'Demon One',
            'malice': 'deception'
        }
        processed_data = preprocess(raw_data, DemonSchema)
        self.assertEqual(processed_data['id'], raw_data['id'])
        self.assertEqual(processed_data['name'], raw_data['name'])
        self.assertEqual(processed_data['malice'], raw_data['malice'])

    def test_preprocess_legion_data(self):
        raw_data = {
            'id': 'legion-001',
            'name': 'Legion One',
            'size': 1000
        }
        processed_data = preprocess(raw_data, LegionSchema)
        self.assertEqual(processed_data['id'], raw_data['id'])
        self.assertEqual(processed_data['name'], raw_data['name'])
        self.assertEqual(processed_data['size'], raw_data['size'])

if __name__ == '__main__':
    unittest.main()