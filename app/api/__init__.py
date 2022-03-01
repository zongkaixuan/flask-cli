# -*- encoding: utf-8 -*-
from flask_restx import Api


authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-Token'
    }
}

api = Api(version='2.0', title='Demo Swagger', description='Demo Swagger', authorizations=authorizations)
api.namespaces.pop(0)
ns = api.namespace('v1', description='Demo API')
