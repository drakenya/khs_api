from app import db

class Name(db.Model):
    __tablename__ = 'names'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    full_name = db.Column(db.String(128))
    email = db.Column(db.String(128))

    fsgroup_id = db.Column(db.Integer, db.ForeignKey('fsgroups.id'))

    fsgroup = db.relationship('Fsgroup')

    def __init__(self, first_name, last_name, email, id=None, fsgroup_id=None):
        if id:
            self.id = id

        if fsgroup_id:
            self.fsgroup_id = fsgroup_id

        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + ' ' + last_name
        self.email = email