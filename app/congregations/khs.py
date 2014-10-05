from app.lib.khs import KhsDataBase


class KhsDataCongregations(KhsDataBase):
    def __init__(self, directory):
        super().__init__(directory)
        self._file += '/congregations.dbf'
        self._special_fields['phone'] = ['cellphone', 'ecellphone', 'econgphone']
        self._remap_fields = {'congregati':'congregation'}
        self._primary_key = 'id'