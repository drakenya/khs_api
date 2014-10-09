from app import db


class Weekly(db.Model):
    __tablename__ = 'weeklies'

    date = db.Column(db.Date, primary_key=True)

    bible_study_date = db.Column(db.Date, db.ForeignKey('bible_studies.date'))
    tms_date = db.Column(db.Date, db.ForeignKey('tmses.date'))
    service_meeting_date = db.Column(db.Date, db.ForeignKey('service_meetings.date'))

    bible_study = db.relationship('BibleStudy')
    tms = db.relationship('Tms')
    service_meeting = db.relationship('ServiceMeeting')

    def __init__(self, date, bible_study_date=None, tms_date=None, service_meeting_date=None):
        self.date = date
        self.bible_study_date = bible_study_date
        self.tms_date = tms_date
        self.service_meeting_date = service_meeting_date