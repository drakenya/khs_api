from flask import Response, jsonify
from flask.json import dumps
from flask.ext.classy import FlaskView, route

from app import app, api, db
from app.speakers.models import Speaker
from app.speakers.khs import KhsDataSpeakers

from app.lib.alchemy import AlchemyEncoder


class SpeakersView(FlaskView):
    @route('/')
    def index(self):
        return Response(dumps(Speaker.query.all(), cls=AlchemyEncoder, indent=2), mimetype='application/json')

    @route('/<int:id>/')
    def get(self, id):
        return Response(dumps(Speaker.query.filter_by(id=id).first(), cls=AlchemyEncoder, indent=2), mimetype='application/json')

    @route('/khs/')
    def khs_index(self):
        results = KhsDataSpeakers(app.config['KHS_DATA_PATH']).get()
        return Response(dumps(results, indent=2), mimetype='application/json')

    @route('/khs/<int:id>/')
    def khs(self, id):
        results = KhsDataSpeakers(app.config['KHS_DATA_PATH']).get(id)
        return Response(dumps(results, indent=2), mimetype='application/json')

SpeakersView.register(app)