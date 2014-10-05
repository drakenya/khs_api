from app import db


class Congregation(db.Model):
    __tablename__ = 'congregations'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    def __init__(self, name, id=None):
        self.id = id

        self.name = name

    def __iter__(self):
        return {
            'id': self.id,
            'name': self.name
        }.iteritems()