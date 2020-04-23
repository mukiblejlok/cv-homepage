from flask import jsonify

from . import api

VERSION = 0.1


@api.route('/version', methods=['GET'])
def api_version():
    return jsonify(VERSION)
