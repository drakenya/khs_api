from app import db

class Name(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)

    def __init__(self, name):
        self.name = name


    def __repr__(self):
        return '<Name %r>' % self.name