import os
import json
from collections import defaultdict
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


class ServiceMeetingList(Resource):
    def get(self):
        return classes.KhsDataServiceMeeting(app.config['data_path']).get()

class ServiceMeeting(Resource):
    def get(self, id):
        return classes.KhsDataServiceMeeting(app.config['data_path']).get(id)

api.add_resource(ServiceMeetingList, '/api/raw/servicemeeting')
api.add_resource(ServiceMeeting, '/api/raw/servicemeeting/<string:id>')


class TmsList(Resource):
    def get(self):
        return classes.KhsDataTms(app.config['data_path']).get()


class Tms(Resource):
    def get(self, id):
        return classes.KhsDataTms(app.config['data_path']).get(id)

api.add_resource(TmsList, '/api/raw/tms')
api.add_resource(Tms, '/api/raw/tms/<string:id>')


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
            for k in ['sound', 'mic1', 'mic2', 'mic3', 'mic4', 'stage', 'attendant1', 'attendant2', 'attendant3']:
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
            self._outlines[id] = {'title': outline['title'], 'id': outline['outline']}

        return self._outlines[id]

    def _get_speaker(self, id):
        if not id in self._speakers:
            speaker = classes.KhsDataSpeakers(app.config['data_path']).get(id)
            speaker_ids = {
                'Andrew Kroll': 27,
                'Marty Kroll': 2,
                'Ronald Brooks Jr.': 1,
                'Matthew Burns': 15,
                'Michael Smith': 49,
                'Edward Tchissi': 13,
                'Brady Kroll': 28,
                'Anthony Pasquini': 40
            }
            self._speakers[id] = {'name': speaker['speaker'], 'id': speaker_ids[speaker['speaker']]}

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
    _names = {}

    def __init__(self):
        self._congregations = {}
        self._outlines = {}
        self._speakers = {}
        self._names = {}

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

            if s['chairman'] is not 0:
                print(s['chairman'])
                chairman = self._get_name(s['chairman'])
                date['chairman'] = chairman

            if s['reader'] is not 0:
                print(s['reader'])
                reader = self._get_name(s['reader'])
                date['reader'] = reader

            if len(date) > 1:
                schedule.append(date)

        return schedule

api.add_resource(IncomingScheduleList, '/api/clean/incoming_schedule')


class TmsScheduleList(Resource):
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

        for s in classes.KhsDataTms(app.config['data_path']).get():
            tree = lambda: defaultdict(tree)
            date = defaultdict(tree)
            date['date'] = s['date']

            # bh
            if 'bh_id' in s and s['bh_id'] is not 0:
                date['bh']['title'] = s['bh']
                date['bh']['speaker'] = self._get_name(s['bh_id'])

            # ms1, ms2, ms3
            for k in [1, 2, 3]:
                talk_key = 'talk' + str(k)
                title_key = talk_key
                speaker_key = 'talk' + str(k) + '_id'
                assistant_key = 'assist' + str(k) + '_id'

                if speaker_key in s and s[speaker_key] is not 0:
                    date[talk_key]['title'] = s[title_key]
                    date[talk_key]['speaker'] = self._get_name(s[speaker_key])

                if assistant_key in s and s[assistant_key] is not 0:
                    date[talk_key]['assistant'] = self._get_name(s[assistant_key])

            if len(date) > 1:
                schedule.append(date)

        return schedule

api.add_resource(TmsScheduleList, '/api/clean/tms_schedule')


class ServiceMeetingScheduleList(Resource):
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

        for s in classes.KhsDataServiceMeeting(app.config['data_path']).get():
            tree = lambda: defaultdict(tree)
            date = defaultdict(tree)
            date['date'] = s['date']
            for k in [1, 2, 3, 4]:
                talk_key = 'talk' + str(k)
                title_key = 'subject' + str(k)
                speaker_key = 'name_id_' + str(k)

                if speaker_key in s and s[speaker_key] is not 0:
                    date[talk_key]['title'] = s[title_key]
                    date[talk_key]['speaker'] = self._get_name(s[speaker_key])

            if len(date) > 1:
                schedule.append(date)

        return schedule

api.add_resource(ServiceMeetingScheduleList, '/api/clean/sm_schedule')

if __name__ == '__main__':
    app.config['data_path'] = os.path.dirname(os.path.realpath(__file__)) + '/khs/data'
    app.run(host='0.0.0.0', debug=True)
