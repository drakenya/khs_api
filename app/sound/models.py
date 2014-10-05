from app import db

class Sound(db.Model):
    __tablename__ = 'sound'

    date = db.Column(db.Date, primary_key=True)

    attendant1_id = db.Column(db.Integer, db.ForeignKey('names.id'))
    console_id = db.Column(db.Integer, db.ForeignKey('names.id'))
    mic1_id = db.Column(db.Integer, db.ForeignKey('names.id'))
    mic2_id = db.Column(db.Integer, db.ForeignKey('names.id'))
    stage_id = db.Column(db.Integer, db.ForeignKey('names.id'))

    attendant = db.relationship('Name', foreign_keys='Sound.attendant1_id')
    console = db.relationship('Name', foreign_keys='Sound.console_id')
    mic1 = db.relationship('Name', foreign_keys='Sound.mic1_id')
    mic2 = db.relationship('Name', foreign_keys='Sound.mic2_id')
    stage = db.relationship('Name', foreign_keys='Sound.stage_id')


    def __init__(self, date=None, attendant1_id=None, mic1_id=None, mic2_id=None, console_id=None, stage_id=None):
        self.date = date
        self.attendant1_id = attendant1_id
        self.mic1_id = mic1_id
        self.mic2_id = mic2_id
        self.console_id = console_id
        self.stage_id = stage_id