from app import app, db
from config import config_path
import datetime

from app.lib.loaddb import LoadDb

app.config.from_object(config_path)

LoadDb.load()