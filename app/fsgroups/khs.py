from app.lib.khs import KhsDataBase

class KhsDataFsgroups(KhsDataBase):
    def __init__(self, directory):
        super().__init__(directory)
        self._file += '/fsgroups.dbf'
        self._primary_key = 'id'