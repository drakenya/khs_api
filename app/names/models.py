from app import db
from json import dumps

class Name(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    email = db.Column(db.String(128))

    fsgroup_id = db.Column(db.Integer, db.ForeignKey('fsgroups.id'))

    # fsgroup_id: <int>

    def __init__(self, first_name, last_name, email, id=None, fsgroup_id=None):
        if id:
            self.id = id

        if fsgroup_id:
            self.fsgroup_id = fsgroup_id

        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __iter__(self):
        return {
            'id': self.id,
            'fsgroup_id': self.fsgroup_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email
        }.iteritems()