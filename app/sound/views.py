from flask import Response, jsonify
from flask.json import dumps
from flask.ext.classy import FlaskView, route

from app import app, api, db
from app.sound.models import Sound
from app.sound.khs import KhsDataSound

from app.lib.alchemy import AlchemyEncoder


class SoundView(FlaskView):
    @route('/')
    def index(self):
        return Response(dumps(Sound.query.all(), cls=AlchemyEncoder, indent=2), mimetype='application/json')

    @route('/<string:date>/')
    def get(self, date):
        return Response(dumps(Sound.query.filter_by(date=date).first(), cls=AlchemyEncoder, indent=2), mimetype='application/json')

    @route('/schedule/')
    def schedule(self):
        return Response(dumps(Sound.query.all(), cls=AlchemyEncoder, indent=2), mimetype='application/json')

    @route('/khs/')
    def khs_index(self):
        results = KhsDataSound(app.config['KHS_DATA_PATH']).get()
        return Response(dumps(results, indent=2), mimetype='application/json')

    @route('/khs/<string:id>/')
    def khs(self, id):
        results = KhsDataSound(app.config['KHS_DATA_PATH']).get(id)
        return Response(dumps(results, indent=2), mimetype='application/json')

SoundView.register(app)