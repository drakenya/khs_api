from app import db


class Schedule(db.Model):
    __tablename__ = 'schedules'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)

    outline_id = db.Column(db.Integer, db.ForeignKey('outlines.id'))
    speaker_id = db.Column(db.Integer, db.ForeignKey('speakers.id'))
    congregation_id = db.Column(db.Integer, db.ForeignKey('congregations.id'))
    chairman_id = db.Column(db.Integer, db.ForeignKey('names.id'))
    reader_id = db.Column(db.Integer, db.ForeignKey('names.id'))
    host_id = db.Column(db.Integer, db.ForeignKey('names.id'))

    speaker_name_id = db.Column(db.Integer, db.ForeignKey('names.id'))

    outline = db.relationship('Outline')
    speaker = db.relationship('Speaker')
    congregation = db.relationship('Congregation')
    chairman = db.relationship('Name', foreign_keys='Schedule.chairman_id')
    reader = db.relationship('Name', foreign_keys='Schedule.reader_id')
    host = db.relationship('Name', foreign_keys='Schedule.host_id')

    speaker_name = db.relationship('Name', foreign_keys='Schedule.speaker_name_id')

    def __init__(self, date, outline_id, speaker_id, congregation_id, chairman_id, reader_id, host_id, id=None, speaker_name_id=None):
        self.id = id

        self.date = date
        self.outline_id = outline_id
        self.speaker_id = speaker_id
        self.congregation_id = congregation_id
        self.chairman_id = chairman_id
        self.reader_id = reader_id
        self.host_id = host_id
        self.speaker_name_id = speaker_name_id