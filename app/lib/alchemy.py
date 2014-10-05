from json import dumps, JSONEncoder
from datetime import date
from sqlalchemy.ext.declarative import DeclarativeMeta


class AlchemyEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)

                if isinstance(data, date):
                    data = str(data)

                try:
                    dumps(data) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    x = 1
                    # none
            # a json-encodable dict
            return fields

        return JSONEncoder.default(self, obj)