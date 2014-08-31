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


class SoundScheduleList(Resource):
    _names = {}

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

if __name__ == '__main__':
    app.config['data_path'] = os.path.dirname(os.path.realpath(__file__)) + '/khs/data'
    app.run(debug=True)