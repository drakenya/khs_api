from app import db


class BibleStudy(db.Model):
    __tablename__ = 'bible_studies'

    date = db.Column(db.Date, primary_key=True)

    title = db.Column(db.String(128))

    conductor_id = db.Column(db.Integer, db.ForeignKey('names.id'))
    reader_id = db.Column(db.Integer, db.ForeignKey('names.id'))

    conductor = db.relationship('Name', foreign_keys='BibleStudy.conductor_id')
    reader = db.relationship('Name', foreign_keys='BibleStudy.reader_id')

    def __init__(self, date, title, conductor_id, reader_id):
        self.date = date
        self.title = title
        self.conductor_id = conductor_id
        self.reader_id = reader_id