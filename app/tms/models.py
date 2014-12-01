from app import db


class Tms(db.Model):
    __tablename__ = 'tmses'

    date = db.Column(db.Date, primary_key=True)

    bh_title = db.Column(db.String(128))
    talk_1_title = db.Column(db.String(128))
    talk_2_title = db.Column(db.String(128))
    talk_3_title = db.Column(db.String(128))

    bh_id = db.Column(db.Integer, db.ForeignKey('names.id'))
    talk_1_id = db.Column(db.Integer, db.ForeignKey('names.id'))
    talk_2_id = db.Column(db.Integer, db.ForeignKey('names.id'))
    talk_3_id = db.Column(db.Integer, db.ForeignKey('names.id'))
    talk_2_assistant_id = db.Column(db.Integer, db.ForeignKey('names.id'))
    talk_3_assistant_id = db.Column(db.Integer, db.ForeignKey('names.id'))
    review_reader_id = db.Column(db.Integer, db.ForeignKey('names.id'))

    bh = db.relationship('Name', foreign_keys='Tms.bh_id')
    talk_1 = db.relationship('Name', foreign_keys='Tms.talk_1_id')
    talk_2 = db.relationship('Name', foreign_keys='Tms.talk_2_id')
    talk_3 = db.relationship('Name', foreign_keys='Tms.talk_3_id')
    talk_1_assistant = db.relationship('Name', foreign_keys='Tms.talk_2_assistant_id')
    talk_2_assistant = db.relationship('Name', foreign_keys='Tms.talk_3_assistant_id')
    review_reader = db.relationship('Name', foreign_keys='Tms.review_reader_id')

    def __init__(self, date, bh_id, talk_1_id, talk_2_id, talk_3_id, talk_2_assistant_id, talk_3_assistant_id, bh_title, talk_1_title, talk_2_title, talk_3_title, review_reader_id):
        self.date = date
        self.bh_id = bh_id
        self.talk_1_id = talk_1_id
        self.talk_2_id = talk_2_id
        self.talk_3_id = talk_3_id
        self.talk_2_assistant_id = talk_2_assistant_id
        self.talk_3_assistant_id = talk_3_assistant_id
        self.bh_title = bh_title
        self.talk_1_title = talk_1_title
        self.talk_2_title = talk_2_title
        self.talk_3_title = talk_3_title
        self.review_reader_id = review_reader_id