from flask import Response, jsonify
from flask.json import dumps
from flask.ext.classy import FlaskView, route

from app import app, api, db
from app.names.models import Name
from app.names.khs import KhsDataNames

from app.lib.alchemy import AlchemyEncoder


class NamesView(FlaskView):
    @route('/')
    def index(self):
        return Response(dumps(Name.query.all(), cls=AlchemyEncoder, indent=2), mimetype='application/json')

    @route('/<int:id>/')
    def get(self, id):
        return Response(dumps(Name.query.filter_by(id=id).first(), cls=AlchemyEncoder, indent=2), mimetype='application/json')

    @route('/khs/')
    def khs_index(self):
        results = KhsDataNames(app.config['KHS_DATA_PATH']).get()
        return Response(dumps(results, indent=2), mimetype='application/json')

    @route('/khs/<int:id>/')
    def khs(self, id):
        results = KhsDataNames(app.config['KHS_DATA_PATH']).get(id)
        return Response(dumps(results, indent=2), mimetype='application/json')

NamesView.register(app)