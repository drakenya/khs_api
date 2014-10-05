from config.base import *

SQLALCHEMY_DATABASE_URI = 'sqlite:////' + basedir + '/../../data/db.sqlite'
KHS_DATA_PATH = basedir + '/../../khs_data'

DEBUG = True