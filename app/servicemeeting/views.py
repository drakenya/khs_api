from flask import Response, jsonify
from flask.json import dumps
from flask.ext.classy import FlaskView, route

from app import app, api, db
from app.servicemeeting.models import ServiceMeeting
from app.servicemeeting.khs import KhsDataServiceMeeting

from app.lib.alchemy import AlchemyEncoder


class ServiceMeetingView(FlaskView):
    @route('/')
    def index(self):
        return Response(dumps(ServiceMeeting.query.all(), cls=AlchemyEncoder, indent=2), mimetype='application/json')

    @route('/<string:id>/')
    def get(self, id):
        return Response(dumps(ServiceMeeting.query.filter_by(date=id).first(), cls=AlchemyEncoder, indent=2), mimetype='application/json')

    @route('/khs/')
    def khs_index(self):
        results = KhsDataServiceMeeting(app.config['KHS_DATA_PATH']).get()
        return Response(dumps(results, indent=2), mimetype='application/json')

    @route('/khs/<int:id>/')
    def khs(self, id):
        results = KhsDataServiceMeeting(app.config['KHS_DATA_PATH']).get(id)
        return Response(dumps(results, indent=2), mimetype='application/json')

ServiceMeetingView.register(app)