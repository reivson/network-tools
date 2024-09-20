from flask import Blueprint

bp = Blueprint('network_tests', __name__, url_prefix='/network')

from . import routes