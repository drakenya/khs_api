from app import db


class Speaker(db.Model):
    __tablename__ = 'speakers'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    name_id = db.Column(db.Integer, db.ForeignKey('names.id'))

    name = db.relationship('Name')

    def __init__(self, first_name, last_name, id=None, name_id=None):
        self.id = id

        self.first_name = first_name
        self.last_name = last_name
        self.name_id = name_id