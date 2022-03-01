# -*- encoding: utf-8 -*-
from flask_restx import Resource
from app.api import ns
from flask import request


@ns.route('/api/test', endpoint='api/test', methods=['GET', ])
class Dna2DbApi(Resource):
    def get(self):
        pass
