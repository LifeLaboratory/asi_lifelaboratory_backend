# coding=utf-8
import os
import sys

sys.path.append(os.getcwd()+'/../')
sys.path.append(os.getcwd()+'../')
import flask
from flask_restful import Api
from app.route.route_list import ROUTES


_app = flask.Flask(__name__, static_folder="print_form")
_app.config['JSON_AS_ASCII'] = False
api = Api(_app)
HEADER = {'Access-Control-Allow-Origin': '*'}


@_app.errorhandler(404)
def not_found(error):
    return {'error': 'Not found'}, 404


if __name__ == '__main__':
    try:
        for route, route_class in ROUTES.items():
            api.add_resource(route_class, route)
        _app.run(host='0.0.0.0', port=80, threaded=True)
    except Exception as e:
        print('Main except = ', e)
