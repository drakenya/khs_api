from app import db


class Outline(db.Model):
    __tablename__ = 'outlines'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    def __init__(self, name, id=None):
        self.id = id

        self.name = name