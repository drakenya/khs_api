from app import db


class Outgoing(db.Model):
    __tablename__ = 'outgoings'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)

    outline_id = db.Column(db.Integer, db.ForeignKey('outlines.id'))
    speaker_id = db.Column(db.Integer, db.ForeignKey('speakers.id'))
    congregation_id = db.Column(db.Integer, db.ForeignKey('congregations.id'))

    outline = db.relationship('Outline')
    speaker = db.relationship('Speaker')
    congregation = db.relationship('Congregation')

    def __init__(self, date, outline_id, speaker_id, congregation_id):
        self.date = date
        self.outline_id = outline_id
        self.speaker_id = speaker_id
        self.congregation_id = congregation_id