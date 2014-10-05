from app import app, db
from config import config_path

from app.fsgroups.models import  Fsgroup
from app.names.models import Name

from app.fsgroups.khs import KhsDataFsgroups
from app.names.khs import KhsDataNames

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
    db.session.commit()

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
    db.session.commit()