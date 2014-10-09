from app.lib.khs import KhsDataBase


class KhsDataTms(KhsDataBase):
    def __init__(self, directory):
        super().__init__(directory)
        self._file += '/tms.dbf'
        self._primary_key = 'date'