from app import db


class ServiceMeeting(db.Model):
    __tablename__ = 'service_meetings'

    date = db.Column(db.Date, primary_key=True)

    talk_1_title = db.Column(db.String(128))
    talk_2_title = db.Column(db.String(128))
    talk_3_title = db.Column(db.String(128))
    talk_4_title = db.Column(db.String(128))

    talk_1_id = db.Column(db.Integer, db.ForeignKey('names.id'))
    talk_2_id = db.Column(db.Integer, db.ForeignKey('names.id'))
    talk_3_id = db.Column(db.Integer, db.ForeignKey('names.id'))
    talk_4_id = db.Column(db.Integer, db.ForeignKey('names.id'))

    talk_1 = db.relationship('Name', foreign_keys='ServiceMeeting.talk_1_id')
    talk_2 = db.relationship('Name', foreign_keys='ServiceMeeting.talk_2_id')
    talk_3 = db.relationship('Name', foreign_keys='ServiceMeeting.talk_3_id')
    talk_3 = db.relationship('Name', foreign_keys='ServiceMeeting.talk_4_id')

    def __init__(self, date, talk_1_id, talk_2_id, talk_3_id, talk_4_id, talk_1_title, talk_2_title, talk_3_title, talk_4_title):
        self.date = date
        self.talk_1_id = talk_1_id
        self.talk_2_id = talk_2_id
        self.talk_3_id = talk_3_id
        self.talk_4_id = talk_4_id
        self.talk_1_title = talk_1_title
        self.talk_2_title = talk_2_title
        self.talk_3_title = talk_3_title
        self.talk_4_title = talk_4_title