import os
import json
from khs import classes
from flask import Flask
from flask.ext.restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

data_path = ''


class NamesList(Resource):
    def get(self):
        return classes.KhsDataNames(app.config['data_path']).get()


class Names(Resource):
    def get(self, id):
        return classes.KhsDataNames(app.config['data_path']).get(id)

api.add_resource(NamesList, '/api/raw/names')
api.add_resource(Names, '/api/raw/names/<string:id>')


class SoundList(Resource):
    def get(self):
        return classes.KhsDataSound(app.config['data_path']).get()


class Sound(Resource):
    def get(self, id):
        classes.KhsDataSound(app.config['data_path']).get(id)

api.add_resource(SoundList, '/api/raw/sound')
api.add_resource(Sound, '/api/raw/sound/<string:id>')


class CongregationsList(Resource):
    def get(self):
        return classes.KhsDataCongregations(app.config['data_path']).get()


class Congregations(Resource):
    def get(self, id):
        return classes.KhsDataCongregations(app.config['data_path']).get(id)

api.add_resource(CongregationsList, '/api/raw/congregations')
api.add_resource(Congregations, '/api/raw/congregations/<string:id>')


class SpeakersList(Resource):
    def get(self):
        return classes.KhsDataSpeakers(app.config['data_path']).get()


class Speakers(Resource):
    def get(self, id):
        return classes.KhsDataSpeakers(app.config['data_path']).get(id)

api.add_resource(SpeakersList, '/api/raw/speakers')
api.add_resource(Speakers, '/api/raw/speakers/<string:id>')


class OutgoingList(Resource):
    def get(self):
        return classes.KhsDataOutgoing(app.config['data_path']).get()


class Outgoing(Resource):
    def get(self, id):
        return classes.KhsDataOutgoing(app.config['data_path']).get(id)

api.add_resource(OutgoingList, '/api/raw/outgoing')
api.add_resource(Outgoing, '/api/raw/outgoing/<string:id>')


class OutlinesList(Resource):
    def get(self):
        return classes.KhsDataOutlines(app.config['data_path']).get()


class Outlines(Resource):
    def get(self, id):
        return classes.KhsDataOutlines(app.config['data_path']).get(id)

api.add_resource(OutlinesList, '/api/raw/outlines')
api.add_resource(Outlines, '/api/raw/outlines/<string:id>')


class ScheduleList(Resource):
    def get(self):
        return classes.KhsDataSchedule(app.config['data_path']).get()


class Schedule(Resource):
    def get(self, id):
        return classes.KhsDataSchedule(app.config['data_path']).get(id)

api.add_resource(ScheduleList, '/api/raw/schedule')
api.add_resource(Schedule, '/api/raw/schedule/<string:id>')


class SoundScheduleList(Resource):
    _names = {}

    def __init__(self):
        self._names = {}

    def _get_name(self, id):
        if not id in self._names:
            name = classes.KhsDataNames(app.config['data_path']).get(id)
            self._names[id] = {'id': name['id'],
                               'firstlast': name['firstlast'],
                               'email': name['email']
            }

        return self._names[id]

    def get(self):
        schedule = []

        for s in classes.KhsDataSound(app.config['data_path']).get():
            date = {'date': s['date']}
            for k in ['sound', 'mic1', 'mic2', 'mic3', 'mic4', 'stage']:
                if s[k] is not 0:
                    date[k] = self._get_name(s[k])

            if len(date) > 1:
                schedule.append(date)

        return schedule

api.add_resource(SoundScheduleList, '/api/clean/sound_schedule')


class OutgoingScheduleList(Resource):
    _congregations = {}
    _outlines = {}
    _speakers = {}

    def __init__(self):
        self._congregations = {}
        self._outlines = {}
        self._speakers = {}

    def _get_congregation(self, id):
        if not id in self._congregations:
            congregation = classes.KhsDataCongregations(app.config['data_path']).get(id)
            self._congregations[id] = {'name': congregation['congregation']}

        return self._congregations[id]

    def _get_outline(self, id):
        if not id in self._outlines:
            outline = classes.KhsDataOutlines(app.config['data_path']).get(id)
            self._outlines[id] = {'title': outline['title']}

        return self._outlines[id]

    def _get_speaker(self, id):
        if not id in self._speakers:
            speaker = classes.KhsDataSpeakers(app.config['data_path']).get(id)
            self._speakers[id] = {'name': speaker['speaker']}

        return self._speakers[id]

    def get(self):
        schedule = []

        for s in classes.KhsDataOutgoing(app.config['data_path']).get():
            date = {'date': s['date']}

            if s['congregation'] is not 0:
                congregation = self._get_congregation(s['congregation'])
                date['congregation'] = congregation

            if s['outline'] is not 0:
                outline = self._get_outline(s['outline'])
                date['outline'] = outline

            if s['speaker'] is not 0:
                speaker = self._get_speaker(s['speaker'])
                date['speaker'] = speaker

            if len(date) > 1:
                schedule.append(date)

        return schedule

api.add_resource(OutgoingScheduleList, '/api/clean/outgoing_schedule')


class IncomingScheduleList(Resource):
    _congregations = {}
    _outlines = {}
    _speakers = {}

    def __init__(self):
        self._congregations = {}
        self._outlines = {}
        self._speakers = {}

    def _get_congregation(self, id):
        if not id in self._congregations:
            congregation = classes.KhsDataCongregations(app.config['data_path']).get(id)
            self._congregations[id] = {'name': congregation['congregation']}

        return self._congregations[id]

    def _get_outline(self, id):
        if not id in self._outlines:
            outline = classes.KhsDataOutlines(app.config['data_path']).get(id)
            self._outlines[id] = {'title': outline['title']}

        return self._outlines[id]

    def _get_speaker(self, id):
        if not id in self._speakers:
            speaker = classes.KhsDataSpeakers(app.config['data_path']).get(id)
            self._speakers[id] = {'name': speaker['speaker']}

        return self._speakers[id]

    def get(self):
        schedule = []

        for s in classes.KhsDataSchedule(app.config['data_path']).get():
            date = {'date': s['date']}

            if s['congregation'] is not 0:
                congregation = self._get_congregation(s['congregation'])
                date['congregation'] = congregation

            if s['outline'] is not 0:
                outline = self._get_outline(s['outline'])
                date['outline'] = outline

            if s['speaker_id'] is not 0:
                speaker = self._get_speaker(s['speaker_id'])
                date['speaker'] = speaker

            if len(date) > 1:
                schedule.append(date)

        return schedule

api.add_resource(IncomingScheduleList, '/api/clean/incoming_schedule')

if __name__ == '__main__':
    app.config['data_path'] = os.path.dirname(os.path.realpath(__file__)) + '/khs/data'
    app.run(host='0.0.0.0', debug=True)
