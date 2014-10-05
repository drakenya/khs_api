from app import db

class Fsgroup(db.Model):
    __tablename__ = 'fsgroups'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    address = db.Column(db.String(128))
    overseer = db.Column(db.String(128))

    names = db.relationship('Name')

    def __init__(self, name, address, overseer, id=None):
        self.id = id

        self.name = name
        self.address = address
        self.overseer = overseer