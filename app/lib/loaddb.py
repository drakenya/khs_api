from app import app, db
from config import config_path
import datetime

from app.fsgroups.models import Fsgroup
from app.names.models import Name
from app.sound.models import Sound
from app.congregations.models import Congregation
from app.outlines.models import Outline
from app.speakers.models import Speaker
from app.outgoing.models import Outgoing
from app.schedule.models import Schedule
from app.tms.models import Tms
from app.servicemeeting.models import ServiceMeeting
from app.biblestudy.models import BibleStudy
from app.weekly.models import Weekly

from app.fsgroups.khs import KhsDataFsgroups
from app.names.khs import KhsDataNames
from app.sound.khs import KhsDataSound
from app.congregations.khs import KhsDataCongregations
from app.outlines.khs import KhsDataOutlines
from app.speakers.khs import KhsDataSpeakers
from app.outgoing.khs import KhsDataOutgoing
from app.schedule.khs import KhsDataSchedule
from app.tms.khs import KhsDataTms
from app.servicemeeting.khs import KhsDataServiceMeeting
from app.biblestudy.khs import KhsDataBibleStudy


class LoadDb():
    @staticmethod
    def load():
        # Refresh the database
        db.drop_all()
        db.create_all()

        # load fsgroups
        fsgroups = KhsDataFsgroups(app.config['KHS_DATA_PATH']).get()
        for fsgroup in fsgroups:
            new_fsgroup = Fsgroup(
                id=fsgroup['id'],
                name=fsgroup['fsgroup'],
                address=fsgroup['address'],
                overseer=fsgroup['overseer']
            )

            db.session.add(new_fsgroup)

        # load names
        names = KhsDataNames(app.config['KHS_DATA_PATH']).get()
        for name in names:
            new_name = Name(
                id=name['id'],
                fsgroup_id=name['fsgroup_id'],
                first_name=name['firstname'],
                last_name=name['lastname'],
                full_name=name['firstlast'],
                email=name['email']
            )

            db.session.add(new_name)

        # load sound (schedule)
        sound = KhsDataSound(app.config['KHS_DATA_PATH']).get()
        for day in sound:
            new_day = Sound(
                date=datetime.datetime.strptime(day['date'], '%Y-%m-%d').date(),
                attendant1_id=day['attendant1'] if day['attendant1'] else None,
                console_id=day['sound'] if day['sound'] else None,
                mic1_id=day['mic1'] if day['mic1'] else None,
                mic2_id=day['mic2'] if day['mic2'] else None,
                stage_id=day['stage'] if day['stage'] else None,
            )

            valid = False
            for key in ['attendant1', 'sound', 'mic1', 'mic2', 'stage']:
                if day[key]:
                    valid = True

            if valid:
                db.session.add(new_day)

        # load congregations
        congregations = KhsDataCongregations(app.config['KHS_DATA_PATH']).get()
        for congregation in congregations:
            new_congregation = Congregation(
                id=congregation['id'],
                name=congregation['congregation'],
            )

            db.session.add(new_congregation)

        # load outlines
        outlines = KhsDataOutlines(app.config['KHS_DATA_PATH']).get()
        for outline in outlines:
            new_outline = Outline(
                id=outline['outline'],
                name=outline['title'],
            )

            db.session.add(new_outline)

        # load speakers
        speakers = KhsDataSpeakers(app.config['KHS_DATA_PATH']).get()
        for speaker in speakers:
            new_speaker = Speaker(
                id=speaker['speaker_id'],
                first_name=speaker['firstname'],
                last_name=speaker['lastname'],
            )

            name = Name.query.filter_by(first_name=new_speaker.first_name, last_name=new_speaker.last_name).first()

            if name:
                new_speaker.name = name

            db.session.add(new_speaker)

        # load outgoing (schedule)
        outgoing = KhsDataOutgoing(app.config['KHS_DATA_PATH']).get()
        for day in outgoing:
            new_outgoing = Outgoing(
                date=datetime.datetime.strptime(day['date'], '%Y-%m-%d').date(),
                outline_id=day['outline'] if day['outline'] else None,
                speaker_id=day['speaker'] if day['speaker'] else None,
                congregation_id=day['congregation'] if day['congregation'] else None
            )

            valid = False
            for key in ['congregation', 'outline', 'speaker']:
                if day[key]:
                    valid = True

            if valid:
                db.session.add(new_outgoing)

        # load schedule (schedule)
        schedule = KhsDataSchedule(app.config['KHS_DATA_PATH']).get()
        for day in schedule:
            new_schedule = Schedule(
                date=datetime.datetime.strptime(day['date'], '%Y-%m-%d').date(),
                outline_id=day['outline'] if day['outline'] else None,
                speaker_id=day['speaker_id'] if day['speaker_id'] else None,
                congregation_id=day['congregation'] if day['congregation'] else None,
                chairman_id=day['chairman'] if day['chairman'] else None,
                reader_id=day['reader'] if day['reader'] else None
            )

            valid = False
            for key in ['congregation', 'outline', 'speaker_id', 'chairman', 'reader']:
                if day[key]:
                    valid = True

            if valid:
                db.session.add(new_schedule)

        # load tms (schedule)
        schedule = KhsDataTms(app.config['KHS_DATA_PATH']).get()
        for day in schedule:
            new_schedule = Tms(
                date=datetime.datetime.strptime(day['date'], '%Y-%m-%d').date(),
                bh_id=day['bh_id'] if day['bh_id'] else None,
                talk_1_id=day['talk1_id'] if day['talk1_id'] else None,
                talk_2_id=day['talk2_id'] if day['talk2_id'] else None,
                talk_3_id=day['talk3_id'] if day['talk3_id'] else None,
                talk_2_assistant_id=day['assist2_id'] if day['assist2_id'] else None,
                talk_3_assistant_id=day['assist3_id'] if day['assist3_id'] else None,
                bh_title=day['bh'] if day['bh'] else None,
                talk_1_title=day['talk1'] if day['talk1'] else None,
                talk_2_title=day['talk2'] if day['talk2'] else None,
                talk_3_title=day['talk3'] if day['talk3'] else None
            )

            valid = False
            for key in ['bh_id', 'talk1_id', 'talk2_id', 'talk3_id']:
                if day[key]:
                    valid = True

            if valid:
                db.session.add(new_schedule)

        # load servicemeeting (schedule)
        schedule = KhsDataServiceMeeting(app.config['KHS_DATA_PATH']).get()
        for day in schedule:
            new_schedule = ServiceMeeting(
                date=datetime.datetime.strptime(day['date'], '%Y-%m-%d').date(),
                talk_1_id=day['name_id_1'] if day['name_id_1'] else None,
                talk_2_id=day['name_id_2'] if day['name_id_2'] else None,
                talk_3_id=day['name_id_3'] if day['name_id_3'] else None,
                talk_4_id=day['name_id_4'] if day['name_id_4'] else None,
                talk_1_title=day['subject1'] if day['subject1'] else None,
                talk_2_title=day['subject2'] if day['subject2'] else None,
                talk_3_title=day['subject3'] if day['subject3'] else None,
                talk_4_title=day['subject4'] if day['subject4'] else None
            )

            valid = False
            for key in ['name_id_1', 'name_id_2', 'name_id_3', 'name_id_4']:
                if day[key]:
                    valid = True

            if valid:
                db.session.add(new_schedule)

        # load biblestudy (schedule)
        schedule = KhsDataBibleStudy(app.config['KHS_DATA_PATH']).get()
        for day in schedule:
            new_schedule = BibleStudy(
                date=datetime.datetime.strptime(day['date'], '%Y-%m-%d').date(),
                conductor_id=day['conductor'] if day['conductor'] else None,
                reader_id=day['reader'] if day['reader'] else None,
                title=day['material'] if day['material'] else None
            )

            valid = False
            for key in ['conductor', 'reader']:
                if day[key]:
                    valid = True

            if valid:
                db.session.add(new_schedule)

        # load weekly (meta-schedule)
        meetings = BibleStudy.query.all()
        for meeting in meetings:
            new_weekly = Weekly(date=meeting.date)
            new_weekly.bible_study = meeting

            db.session.add(new_weekly)

        meetings = Tms.query.all()
        for meeting in meetings:
            weekly = Weekly.query.filter_by(date=meeting.date).first()
            if not weekly:
                weekly = Weekly(date=meeting.date)
                db.session.add(weekly)

            weekly.tms = meeting

        meetings = ServiceMeeting.query.all()
        for meeting in meetings:
            weekly = Weekly.query.filter_by(date=meeting.date).first()
            if not weekly:
                weekly = Weekly(date=meeting.date)
                db.session.add(weekly)

            weekly.service_meeting = meeting

        db.session.commit()