from flask import Response, jsonify
from flask.json import dumps
from flask.ext.classy import FlaskView, route

from app import app, api, db
from app.weekly.models import Weekly

from app.lib.alchemy import AlchemyEncoder


class WeeklyView(FlaskView):
    @route('/')
    def index(self):
        return Response(dumps(Weekly.query.all(), cls=AlchemyEncoder, indent=2), mimetype='application/json')

    @route('/<string:id>/')
    def get(self, id):
        return Response(dumps(Weekly.query.filter_by(id=id).first(), cls=AlchemyEncoder, indent=2), mimetype='application/json')

WeeklyView.register(app)