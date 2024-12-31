from flask import Blueprint, request, jsonify
from models.legion_model import LegionModel
from utils.data_loader import load_legion_data
from utils.logger import log

legion_api_blueprint = Blueprint('legion_api', __name__)

@legion_api_blueprint.route('/api/legion', methods=['GET'])
def get_legions():
    try:
        legions = load_legion_data()
        return jsonify(legions), 200
    except Exception as e:
        log(e)
        return jsonify({"error": "Unable to fetch legions"}), 500

@legion_api_blueprint.route('/api/legion', methods=['POST'])
def create_legion():
    try:
        data = request.json
        legion = LegionModel.create_legion(data)
        return jsonify(legion), 201
    except Exception as e:
        log(e)
        return jsonify({"error": "Unable to create legion"}), 500

@legion_api_blueprint.route('/api/legion/<int:legion_id>', methods=['GET'])
def get_legion(legion_id):
    try:
        legion = LegionModel.get_legion_by_id(legion_id)
        if legion:
            return jsonify(legion), 200
        else:
            return jsonify({"error": "Legion not found"}), 404
    except Exception as e:
        log(e)
        return jsonify({"error": "Unable to fetch legion"}), 500

@legion_api_blueprint.route('/api/legion/<int:legion_id>', methods=['PUT'])
def update_legion(legion_id):
    try:
        data = request.json
        updated_legion = LegionModel.update_legion(legion_id, data)
        if updated_legion:
            return jsonify(updated_legion), 200
        else:
            return jsonify({"error": "Legion not found"}), 404
    except Exception as e:
        log(e)
        return jsonify({"error": "Unable to update legion"}), 500

@legion_api_blueprint.route('/api/legion/<int:legion_id>', methods=['DELETE'])
def delete_legion(legion_id):
    try:
        success = LegionModel.delete_legion(legion_id)
        if success:
            return jsonify({"message": "Legion deleted successfully"}), 200
        else:
            return jsonify({"error": "Legion not found"}), 404
    except Exception as e:
        log(e)
        return jsonify({"error": "Unable to delete legion"}), 500
