from app import db


class OCLM(db.Model):
    __tablename__ = 'oclm'

    date = db.Column(db.Date, primary_key=True)

    chairman_id = db.Column(db.Integer, db.ForeignKey('names.id'))
    prayer_1_id = db.Column(db.Integer, db.ForeignKey('names.id'))
    prayer_2_id = db.Column(db.Integer, db.ForeignKey('names.id'))

    chairman = db.relationship('Name', foreign_keys='OCLM.chairman_id')
    prayer_1 = db.relationship('Name', foreign_keys='OCLM.prayer_1_id')
    prayer_2 = db.relationship('Name', foreign_keys='OCLM.prayer_2_id')

    bible_reading_title = db.Column(db.String(128))

    bible_reading_id = db.Column(db.Integer, db.ForeignKey('names.id'))
    initial_call_id = db.Column(db.Integer, db.ForeignKey('names.id'))
    initial_call_assistant_id = db.Column(db.Integer, db.ForeignKey('names.id'))
    return_visit_id = db.Column(db.Integer, db.ForeignKey('names.id'))
    return_visit_assistant_id = db.Column(db.Integer, db.ForeignKey('names.id'))
    bible_study_id = db.Column(db.Integer, db.ForeignKey('names.id'))
    bible_study_assistant_id = db.Column(db.Integer, db.ForeignKey('names.id'))

    bible_reading = db.relationship('Name', foreign_keys='OCLM.bible_reading_id')
    initial_call = db.relationship('Name', foreign_keys='OCLM.initial_call_id')
    initial_call_assistant = db.relationship('Name', foreign_keys='OCLM.initial_call_assistant_id')
    return_visit = db.relationship('Name', foreign_keys='OCLM.return_visit_id')
    return_visit_assistant = db.relationship('Name', foreign_keys='OCLM.return_visit_assistant_id')
    bible_study = db.relationship('Name', foreign_keys='OCLM.bible_study_id')
    bible_study_assistant = db.relationship('Name', foreign_keys='OCLM.bible_study_assistant_id')

    cbs_title = db.Column(db.String(128))

    cbs_conductor_id = db.Column(db.Integer, db.ForeignKey('names.id'))
    cbs_reader_id = db.Column(db.Integer, db.ForeignKey('names.id'))

    cbs_conductor = db.relationship('Name', foreign_keys='OCLM.cbs_conductor_id')
    cbs_reader = db.relationship('Name', foreign_keys='OCLM.cbs_reader_id')

    talk_title = db.Column(db.String(128))
    living_as_christians_1_title = db.Column(db.String(128))
    living_as_christians_2_title = db.Column(db.String(128))
    digging_for_gems_id = db.Column(db.Integer, db.ForeignKey('names.id'))
    prepare_presentations_id = db.Column(db.Integer, db.ForeignKey('names.id'))
    talk_id = db.Column(db.Integer, db.ForeignKey('names.id'))
    living_as_christians_1_id = db.Column(db.Integer, db.ForeignKey('names.id'))
    living_as_christians_2_id = db.Column(db.Integer, db.ForeignKey('names.id'))
    digging_for_gems = db.relationship('Name', foreign_keys='OCLM.digging_for_gems_id')
    prepare_presentations = db.relationship('Name', foreign_keys='OCLM.prepare_presentations_id')
    talk = db.relationship('Name', foreign_keys='OCLM.talk_id')
    living_as_christians_1 = db.relationship('Name', foreign_keys='OCLM.living_as_christians_1_id')
    living_as_christians_2 = db.relationship('Name', foreign_keys='OCLM.living_as_christians_2_id')


    def __init__(self, **kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])
