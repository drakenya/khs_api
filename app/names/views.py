from flask import Response, jsonify
from flask.json import dumps
from flask.ext.classy import FlaskView, route

from app import app, api, db
from app.names.models import Name
from app.names.khs import KhsDataNames


class NamesView(FlaskView):
    @route('/')
    def index(self):
        # db.create_all()
        return app.config['SQLALCHEMY_DATABASE_URI']
        # args = parser.parse_args()
        # return {'args': args}

    @route('/khs/')
    def khs_index(self):
        results = KhsDataNames(app.config['KHS_DATA_PATH']).get()
        return Response(dumps(results, indent=2), mimetype='application/json')

    @route('/khs/<int:id>/')
    def khs(self, id):
        results = KhsDataNames(app.config['KHS_DATA_PATH']).get(id)
        return Response(dumps(results, indent=2), mimetype='application/json')

NamesView.register(app)