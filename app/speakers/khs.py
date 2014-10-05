from app.lib.khs import KhsDataBase


class KhsDataSpeakers(KhsDataBase):
    def __init__(self, directory):
        super().__init__(directory)
        self._file += '/speakers.dbf'
        self._special_fields['phone'] = ['ecellphone', 'ephone']
        self._remap_fields = {'congregati':'congregation'}
        self._primary_key = 'speaker_id'