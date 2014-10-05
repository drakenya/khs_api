from app import db
from json import dumps

class Fsgroup(db.Model):
    __tablename__ = 'fsgroups'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    address = db.Column(db.String(128))
    overseer = db.Column(db.String(128))

    names = db.relationship("Name")

    # fsgroup_id: <int>

    def __init__(self, name, address, overseer, id=None):
        if id:
            self.id = id

        self.name = name
        self.address = address
        self.overseer = overseer

    def __iter__(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'overseer': self.overseer
        }.iteritems()