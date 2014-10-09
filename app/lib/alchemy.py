from json import dumps, JSONEncoder, loads
from datetime import date
from sqlalchemy.ext.declarative import DeclarativeMeta

from app.names.models import Name
from app.speakers.models import Speaker
from app.congregations.models import Congregation
from app.outlines.models import Outline
from app.biblestudy.models import BibleStudy
from app.tms.models import Tms
from app.servicemeeting.models import ServiceMeeting


class AlchemyEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)

                if isinstance(data, date):
                    data = str(data)

                if isinstance(data, Name)\
                        or isinstance(data, Speaker)\
                        or isinstance(data, Congregation)\
                        or isinstance(data, Outline)\
                        or isinstance(data, BibleStudy)\
                        or isinstance(data, Tms)\
                        or isinstance(data, ServiceMeeting):
                    data = loads(dumps(data, cls=AlchemyEncoder))

                try:
                    dumps(data) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    x = 1
                    # none
            # a json-encodable dict
            return fields

        return JSONEncoder.default(self, obj)