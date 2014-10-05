from app import app, db
from config import config_path

from app.names.models import Name

from app.names.khs import KhsDataNames

app.config.from_object(config_path)

# Refresh the database
db.drop_all()
db.create_all()

# load names
names = KhsDataNames(app.config['KHS_DATA_PATH']).get()
for name in names:
    new_name = Name(
        id=name['id'],
        first_name=name['firstname'],
        last_name=name['lastname'],
        email=name['email']
    )

    db.session.add(new_name)
    db.session.commit()