from app import app, db
from config import config_path
import datetime

from app.fsgroups.models import Fsgroup
from app.names.models import Name
from app.sound.models import Sound

from app.fsgroups.khs import KhsDataFsgroups
from app.names.khs import KhsDataNames
from app.sound.khs import KhsDataSound

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

    db.session.add(new_day)

db.session.commit()