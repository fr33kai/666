from flask import Blueprint
from .agent_api import agent_api_blueprint
from .angel_api import angel_api_blueprint
from .demon_api import demon_api_blueprint
from .legion_api import legion_api_blueprint

api_blueprint = Blueprint('api', __name__, url_prefix='/api')

api_blueprint.register_blueprint(agent_api_blueprint)
api_blueprint.register_blueprint(angel_api_blueprint)
api_blueprint.register_blueprint(demon_api_blueprint)
api_blueprint.register_blueprint(legion_api_blueprint)