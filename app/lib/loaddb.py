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
from app.oclm.models import OCLM

from app.fsgroups.khs import KhsDataFsgroups
from app.names.khs import KhsDataNames
from app.sound.khs import KhsDataSound
from app.congregations.khs import KhsDataCongregations
from app.outlines.khs import KhsDataOutlines
from app.speakers.khs import KhsDataSpeakers
from app.outgoing.khs import KhsDataOutgoing
from app.schedule.khs import KhsDataSchedule
from app.oclm.khs import KhsDataOCLM


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
            speaker_name_id = None
            if day['speaker']:
                speaker = Speaker.query.filter_by(id=day['speaker']).first()
                if speaker:
                    speaker_name_id = speaker.name_id
            new_outgoing = Outgoing(
                date=datetime.datetime.strptime(day['date'], '%Y-%m-%d').date(),
                outline_id=day['outline'] if day['outline'] else None,
                speaker_id=day['speaker'] if day['speaker'] else None,
                congregation_id=day['congregation'] if day['congregation'] else None,
                speaker_name_id=speaker_name_id
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
            speaker_name_id = None
            if day['speaker_id']:
                speaker = Speaker.query.filter_by(id=day['speaker_id']).first()
                if speaker:
                    speaker_name_id = speaker.name_id
            if day['date']:
                new_schedule = Schedule(
                    date=datetime.datetime.strptime(day['date'], '%Y-%m-%d').date(),
                    outline_id=day['outline'] if day['outline'] else None,
                    speaker_id=day['speaker_id'] if day['speaker_id'] else None,
                    congregation_id=day['congregation'] if day['congregation'] else None,
                    chairman_id=day['chairman'] if day['chairman'] else None,
                    reader_id=day['reader'] if day['reader'] else None,
                    host_id=day['host'] if day['host'] else None,
                    speaker_name_id=speaker_name_id,
                )

                valid = False
                for key in ['congregation', 'outline', 'speaker_id', 'chairman', 'reader']:
                    if day[key]:
                        valid = True

                if valid:
                    db.session.add(new_schedule)

        # load OCLM (schedule)
        schedule = KhsDataOCLM(app.config['KHS_DATA_PATH']).get()
        for day in schedule:
            new_schedule = OCLM(
                date=datetime.datetime.strptime(day['date'], '%Y-%m-%d').date(),
                bible_reading_id=day['br1'] if day['br1'] else None,
                bible_reading_title=day['br'] if day['br'] else None,
                initial_call_id=day['ic1'] if day['ic1'] else None,
                initial_call_assistant_id=day['ic_asst1'] if day['ic_asst1'] else None,
                return_visit_id=day['rv1'] if day['rv1'] else None,
                return_visit_assistant_id=day['rv_asst1'] if day['rv_asst1'] else None,
                bible_study_id=day['bs1'] if day['bs1'] else None,
                bible_study_assistant_id=day['bs_asst1'] if day['bs_asst1'] else None,
                cbs_title=day['cbs'] if day['cbs'] else None,
                cbs_conductor_id=day['cbs_conduc'] if day['cbs_conduc'] else None,
                cbs_reader_id=day['cbs_reader'] if day['cbs_reader'] else None,
                chairman_id=day['chairman'] if day['chairman'] else None,
                prayer_1_id=day['prayer1'] if day['prayer1'] else None,
                talk_title=day['talk'] if day['talk'] else None,
                living_as_christians_1_title=day['subject1'] if day['subject1'] else None,
                living_as_christians_2_title=day['subject2'] if day['subject2'] else None,
                digging_for_gems_id=day['gems'] if day['gems'] else None,
                prepare_presentations_id=day['prepare_id'] if day['prepare_id'] else None,
                talk_id=day['talk_id'] if day['talk_id'] else None,
                living_as_christians_1_id=day['name1_id'] if day['name1_id'] else None,
                living_as_christians_2_id=day['name2_id'] if day['name2_id'] else None,
            )

            valid = False
            for key in ['br1', 'ic1', 'rv1', 'bs1', 'cbs_conduc', 'chairman', 'prayer1']:
                if day[key]:
                    valid = True

            if valid:
                db.session.add(new_schedule)

        db.session.commit()
