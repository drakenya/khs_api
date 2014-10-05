from app import db


class Speaker(db.Model):
    __tablename__ = 'speakers'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))

    def __init__(self, first_name, last_name, id=None):
        self.id = id

        self.first_name = first_name
        self.last_name = last_name

    def __iter__(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name
        }.iteritems()