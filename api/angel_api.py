from flask import Blueprint, request, jsonify
from models.angel_model import AngelModel
from utils.data_loader import load_angel_data
from utils.logger import log

angel_api = Blueprint('angel_api', __name__)

@angel_api.route('/api/angel', methods=['GET'])
def get_angels():
    try:
        angels = load_angel_data()
        return jsonify(angels), 200
    except Exception as e:
        log_event("Error in get_angels: " + str(e))
        return jsonify({"error": "Unable to fetch angels"}), 500

@angel_api.route('/api/angel', methods=['POST'])
def create_angel():
    try:
        angel_data = request.json
        new_angel = AngelModel.create_angel(angel_data)
        log_event("AngelCreated", new_angel)
        return jsonify(new_angel), 201
    except Exception as e:
        log_event("Error in create_angel: " + str(e))
        return jsonify({"error": "Unable to create angel"}), 500

@angel_api.route('/api/angel/<int:angel_id>', methods=['GET'])
def get_angel(angel_id):
    try:
        angel = AngelModel.get_angel_by_id(angel_id)
        if angel:
            return jsonify(angel), 200
        else:
            return jsonify({"error": "Angel not found"}), 404
    except Exception as e:
        log_event("Error in get_angel: " + str(e))
        return jsonify({"error": "Unable to fetch angel"}), 500

@angel_api.route('/api/angel/<int:angel_id>', methods=['PUT'])
def update_angel(angel_id):
    try:
        angel_data = request.json
        updated_angel = AngelModel.update_angel(angel_id, angel_data)
        log_event("AngelUpdated", updated_angel)
        return jsonify(updated_angel), 200
    except Exception as e:
        log_event("Error in update_angel: " + str(e))
        return jsonify({"error": "Unable to update angel"}), 500

@angel_api.route('/api/angel/<int:angel_id>', methods=['DELETE'])
def delete_angel(angel_id):
    try:
        result = AngelModel.delete_angel(angel_id)
        if result:
            log_event("AngelDeleted", {"id": angel_id})
            return jsonify({"message": "Angel deleted"}), 200
        else:
            return jsonify({"error": "Angel not found"}), 404
    except Exception as e:
        log_event("Error in delete_angel: " + str(e))
        return jsonify({"error": "Unable to delete angel"}), 500
