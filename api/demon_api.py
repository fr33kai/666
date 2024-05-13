from flask import Blueprint, request, jsonify
from models.demon_model import DemonModel
from utils.data_loader import load_demon_data
from utils.logger import log

demon_api = Blueprint('demon_api', __name__)

@demon_api.route('/api/demon', methods=['POST'])
def create_demon():
    try:
        data = request.get_json()
        demon = DemonModel.create(data)
        log_event('DemonCreated', demon.id)
        return jsonify(demon.to_dict()), 201
    except Exception as e:
        log_event('Error', str(e))
        return jsonify({'error': 'Failed to create demon'}), 500

@demon_api.route('/api/demon/<int:demon_id>', methods=['GET'])
def get_demon(demon_id):
    try:
        demon = DemonModel.get_by_id(demon_id)
        if demon:
            log_event('DemonStatus', demon.id)
            return jsonify(demon.to_dict()), 200
        else:
            return jsonify({'error': 'Demon not found'}), 404
    except Exception as e:
        log_event('Error', str(e))
        return jsonify({'error': 'Failed to retrieve demon'}), 500

@demon_api.route('/api/demon', methods=['GET'])
def get_all_demons():
    try:
        demons = DemonModel.get_all()
        demons_data = [demon.to_dict() for demon in demons]
        log_event('DemonStatus', 'retrieved all demons')
        return jsonify(demons_data), 200
    except Exception as e:
        log_event('Error', str(e))
        return jsonify({'error': 'Failed to retrieve demons'}), 500

@demon_api.route('/api/demon/<int:demon_id>', methods=['PUT'])
def update_demon(demon_id):
    try:
        data = request.get_json()
        demon = DemonModel.update(demon_id, data)
        log_event('DemonUpdated', demon.id)
        return jsonify(demon.to_dict()), 200
    except Exception as e:
        log_event('Error', str(e))
        return jsonify({'error': 'Failed to update demon'}), 500

@demon_api.route('/api/demon/<int:demon_id>', methods=['DELETE'])
def delete_demon(demon_id):
    try:
        demon = DemonModel.delete(demon_id)
        log_event('DemonDeleted', demon_id)
        return jsonify({'message': 'Demon deleted successfully'}), 200
    except Exception as e:
        log_event('Error', str(e))
        return jsonify({'error': 'Failed to delete demon'}), 500

@demon_api.route('/api/demon/load', methods=['POST'])
def load_demons():
    try:
        demons_data = load_demon_data()
        DemonModel.bulk_create(demons_data)
        log_event('DemonsLoaded', 'All demons loaded')
        return jsonify({'message': 'Demons loaded successfully'}), 200
    except Exception as e:
        log_event('Error', str(e))
        return jsonify({'error': 'Failed to load demons'}), 500
