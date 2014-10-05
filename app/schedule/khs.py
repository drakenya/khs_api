from app.lib.khs import KhsDataBase


class KhsDataSchedule(KhsDataBase):
    def __init__(self, directory):
        super().__init__(directory)
        self._file += '/schedule.dbf'
        self._primary_key = 'id'
        self._remap_fields = {'congregati':'congregation'}