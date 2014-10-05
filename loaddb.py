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

from app.fsgroups.khs import KhsDataFsgroups
from app.names.khs import KhsDataNames
from app.sound.khs import KhsDataSound
from app.congregations.khs import KhsDataCongregations
from app.outlines.khs import KhsDataOutlines
from app.speakers.khs import KhsDataSpeakers
from app.outgoing.khs import KhsDataOutgoing
from app.schedule.khs import KhsDataSchedule

app.config.from_object(config_path)

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

db.session.commit()