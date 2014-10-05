from app import db
from json import dumps

class Sound(db.Model):
    __tablename__ = 'sound'

    date = db.Column(db.Date, primary_key=True)

    attendant1_id = db.Column(db.Integer, db.ForeignKey('names.id'))
    console_id = db.Column(db.Integer, db.ForeignKey('names.id'))
    mic1_id = db.Column(db.Integer, db.ForeignKey('names.id'))
    mic2_id = db.Column(db.Integer, db.ForeignKey('names.id'))
    stage_id = db.Column(db.Integer, db.ForeignKey('names.id'))

    # fsgroup_id: <int>

    def __init__(self, date=None, attendant1_id=None, mic1_id=None, mic2_id=None, console_id=None, stage_id=None):
        self.date = date
        self.attendant1_id = attendant1_id
        self.mic1_id = mic1_id
        self.mic2_id = mic2_id
        self.console_id = console_id
        self.stage_id = stage_id

    def __iter__(self):
        return {
            'date': self.date,
            'attendant1_id': self.attendant1_id,
            'console_id': self.console_id,
            'mic1_id': self.mic1_id,
            'mic2_id': self.mic2_id,
            'stage_id': self.stage_id
        }.iteritems()