from flask import Response, jsonify
from flask.json import dumps
from flask.ext.classy import FlaskView, route

from app import app, api, db
from app.fsgroups.models import Fsgroup
from app.fsgroups.khs import KhsDataFsgroups

from app.lib.alchemy import AlchemyEncoder


class FsgroupsView(FlaskView):
    @route('/')
    def index(self):
        return Response(dumps(Fsgroup.query.all(), cls=AlchemyEncoder, indent=2), mimetype='application/json')

    @route('/<int:id>/')
    def get(self, id):
        return Response(dumps(Fsgroup.query.filter_by(id=id).first(), cls=AlchemyEncoder, indent=2), mimetype='application/json')

    @route('/khs/')
    def khs_index(self):
        results = KhsDataFsgroups(app.config['KHS_DATA_PATH']).get()
        return Response(dumps(results, indent=2), mimetype='application/json')

    @route('/khs/<int:id>/')
    def khs(self, id):
        results = KhsDataFsgroups(app.config['KHS_DATA_PATH']).get(id)
        return Response(dumps(results, indent=2), mimetype='application/json')

FsgroupsView.register(app)