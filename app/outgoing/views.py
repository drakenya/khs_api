from flask import Response, jsonify
from flask.json import dumps
from flask.ext.classy import FlaskView, route

from app import app, api, db
from app.outgoing.models import Outgoing
from app.outgoing.khs import KhsDataOutgoing

from app.congregations.models import Congregation
from app.schedule.models import Schedule

from app.lib.alchemy import AlchemyEncoder


class OutgoingView(FlaskView):
    @route('/')
    def index(self):
        return Response(dumps(Outgoing.query.all(), cls=AlchemyEncoder, indent=2), mimetype='application/json')

    @route('/<int:id>/')
    def get(self, id):
        return Response(dumps(Outgoing.query.filter_by(id=id).first(), cls=AlchemyEncoder, indent=2), mimetype='application/json')

    @route('/local/')
    def full(self):
        cong_id = Congregation.query.filter_by(name='Pleasant Hills').first().id
        return Response(dumps(Schedule.query.filter_by(congregation_id=cong_id).all(), cls=AlchemyEncoder, indent=2), mimetype='application/json')

    @route('/khs/')
    def khs_index(self):
        results = KhsDataOutgoing(app.config['KHS_DATA_PATH']).get()
        return Response(dumps(results, indent=2), mimetype='application/json')

    @route('/khs/<int:id>/')
    def khs(self, id):
        results = KhsDataOutgoing(app.config['KHS_DATA_PATH']).get(id)
        return Response(dumps(results, indent=2), mimetype='application/json')

OutgoingView.register(app)