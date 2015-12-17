from flask import Response, jsonify
from flask.json import dumps
from flask.ext.classy import FlaskView, route

from app import app, api, db
from app.oclm.models import OCLM
from app.oclm.khs import KhsDataOCLM

from app.lib.alchemy import AlchemyEncoder


class OCLMView(FlaskView):
    @route('/')
    def index(self):
        return Response(dumps(OCLM.query.all(), cls=AlchemyEncoder, indent=2), mimetype='application/json')

    @route('/<string:id>/')
    def get(self, id):
        return Response(dumps(OCLM.query.filter_by(date=id).first(), cls=AlchemyEncoder, indent=2), mimetype='application/json')

    @route('/khs/')
    def khs_index(self):
        results = KhsDataOCLM(app.config['KHS_DATA_PATH']).get()
        return Response(dumps(results, indent=2), mimetype='application/json')

    @route('/khs/<int:id>/')
    def khs(self, id):
        results = KhsDataOCLM(app.config['KHS_DATA_PATH']).get(id)
        return Response(dumps(results, indent=2), mimetype='application/json')

OCLMView.register(app)