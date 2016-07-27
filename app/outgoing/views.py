from flask import Response, jsonify
from flask.json import dumps
from flask.ext.classy import FlaskView, route

from app import app, api, db
from app.outgoing.models import Outgoing
from app.outgoing.khs import KhsDataOutgoing

from app.congregations.models import Congregation
from app.schedule.models import Schedule
from app.outlines.models import Outline

from app.lib.alchemy import AlchemyEncoder

import sqlalchemy
import pprint


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

    @route('/all/')
    def all(self):
        outgoing_parts = Outgoing.query.join(Outgoing.outline).join(Outgoing.congregation)\
            .with_entities(Outgoing.date, Outgoing.speaker_name_id, Outgoing.outline_id, Outline.name, Congregation.name)\
            .all()

        cong_id = Congregation.query.filter_by(name='Pleasant Hills').first().id
        local_parts = Schedule.query.join(Schedule.outline).join(Schedule.congregation)\
            .with_entities(Schedule.date, Schedule.speaker_name_id, Schedule.outline_id, Outline.name, Congregation.name)\
            .filter(Schedule.congregation_id == cong_id).all()

        all_parts = []
        for part in local_parts + outgoing_parts:
            all_parts.append({
                'date': part.date,
                'speaker_name_id': part.speaker_name_id,
                'title': 'Talk #%d @ %s (%s)' % (part.outline_id, part[4], part[3])
            })

        def date_handler(obj):
            if hasattr(obj, 'isoformat'):
                return obj.isoformat()
            else:
                raise TypeError

        return Response(dumps(all_parts, default=date_handler, indent=2), mimetype='application/json')

    @route('/khs/')
    def khs_index(self):
        results = KhsDataOutgoing(app.config['KHS_DATA_PATH']).get()
        return Response(dumps(results, indent=2), mimetype='application/json')

    @route('/khs/<int:id>/')
    def khs(self, id):
        results = KhsDataOutgoing(app.config['KHS_DATA_PATH']).get(id)
        return Response(dumps(results, indent=2), mimetype='application/json')

OutgoingView.register(app)