from dbfread import DBF
from datetime import date
from re import sub


class KhsDataBase():
    _data = []
    _file = None
    _special_fields = {'phone': []}
    _remap_fields = {}
    _primary_key = ''

    def __init__(self, directory):
        self._data = []
        self._file = directory + '/'

    def get(self, id=None):
        for record in DBF(self._file):
            obj = {}
            for k, v in record.items():
                key = k.lower()

                if isinstance(v, date):
                    v = str(v)

                if key in self._special_fields['phone']:
                    v = self._format_phone(v)

                if key in self._remap_fields:
                    key = self._remap_fields[key]

                obj[key] = v

            if id is None or str(obj[self._primary_key]) == str(id):
                self._data.append(obj)

        if id is None:
            return self._data
        elif len(self._data) == 1:
            return self._data[0]
        else:
            return {}

    def _format_phone(self, v):
        return sub(r"\D", "", v)