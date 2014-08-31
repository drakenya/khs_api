#!/usr/bin/python3

import datetime, json, re
from dbfread import DBF


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

                if isinstance(v, datetime.date):
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
        return re.sub(r"\D", "", v)


class KhsDataBibleStudy(KhsDataBase):
    def __init__(self, directory):
        super().__init__(directory)
        self._file += '/biblestudy.dbf'


class KhsDataCongregations(KhsDataBase):
    def __init__(self, directory):
        super().__init__(directory)
        self._file += '/congregations.dbf'
        self._special_fields['phone'] = ['cellphone', 'ecellphone', 'econgphone']
        self._remap_fields = {'congregati':'congregation'}
        self._primary_key = 'id'


class KhsDataNames(KhsDataBase):
    def __init__(self, directory):
        super().__init__(directory)
        self._file += '/names.dbf'
        self._primary_key = 'id'


class KhsDataOutgoing(KhsDataBase):
    def __init__(self, directory):
        super().__init__(directory)
        self._file += '/outgoing.dbf'
        self._remap_fields = {'congregati':'congregation'}


class KhsDataOutlines(KhsDataBase):
    def __init__(self, directory):
        super().__init__(directory)
        self._file += '/outlines.dbf'
        self._primary_key = 'outline'


class KhsDataSchedule(KhsDataBase):
    def __init__(self, directory):
        super().__init__(directory)
        self._file += '/schedule.dbf'
        self._primary_key = 'id'
        self._remap_fields = {'congregati':'congregation'}


class KhsDataSpeakers(KhsDataBase):
    def __init__(self, directory):
        super().__init__(directory)
        self._file += '/speakers.dbf'
        self._special_fields['phone'] = ['ecellphone', 'ephone']
        self._remap_fields = {'congregati':'congregation'}
        self._primary_key = 'speaker_id'


class KhsDataSound(KhsDataBase):
    def __init__(self, directory):
        super().__init__(directory)
        self._file += '/sound.dbf'
        self._primary_key = 'date'


class KhsDataUser(KhsDataBase):
    def __init__(self, directory):
        super().__init__(directory)
        self._file += '/user.dbf'


if __name__ == '__main__':
    # print(KhsDataBibleStudy('data').serialize())
    # print(KhsDataNames('data').serialize())
    # print(KhsDataSpeakers('data').serialize())
    print(json.dumps(KhsDataSound('data').get(), sort_keys=True, indent=2, separators=(',', ': ')))
    # print(KhsDataUser('data').serialize())
