from flask import Flask
from flask.ext.restful import Api
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)

from app.fsgroups import views as _
from app.names import views as _
from app.sound import views as _

from app.congregations import views as _
from app.outlines import views as _
from app.speakers import views as _
from app.outgoing import views as _
