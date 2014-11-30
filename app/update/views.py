from flask import Response
from flask.ext.classy import FlaskView, route

from app import app
from app.lib.loaddb import LoadDb



class UpdateView(FlaskView):
    @route('/', methods=['POST'])
    def index(self):
        LoadDb.load()
        return Response('')

UpdateView.register(app)