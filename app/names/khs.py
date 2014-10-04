from app.lib.khs import KhsDataBase

class KhsDataNames(KhsDataBase):
    def __init__(self, directory):
        super().__init__(directory)
        self._file += '/names.dbf'
        self._primary_key = 'id'