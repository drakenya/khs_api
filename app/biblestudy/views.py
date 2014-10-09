from flask import Response, jsonify
from flask.json import dumps
from flask.ext.classy import FlaskView, route

from app import app, api, db
from app.biblestudy.models import BibleStudy
from app.biblestudy.khs import KhsDataBibleStudy

from app.lib.alchemy import AlchemyEncoder


class BibleStudyView(FlaskView):
    @route('/')
    def index(self):
        return Response(dumps(BibleStudy.query.all(), cls=AlchemyEncoder, indent=2), mimetype='application/json')

    @route('/<string:id>/')
    def get(self, id):
        return Response(dumps(BibleStudy.query.filter_by(id=id).first(), cls=AlchemyEncoder, indent=2), mimetype='application/json')

    @route('/khs/')
    def khs_index(self):
        results = KhsDataBibleStudy(app.config['KHS_DATA_PATH']).get()
        return Response(dumps(results, indent=2), mimetype='application/json')

    @route('/khs/<int:id>/')
    def khs(self, id):
        results = KhsDataBibleStudy(app.config['KHS_DATA_PATH']).get(id)
        return Response(dumps(results, indent=2), mimetype='application/json')

BibleStudyView.register(app)