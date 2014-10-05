from app.lib.khs import KhsDataBase

class KhsDataSound(KhsDataBase):
    def __init__(self, directory):
        super().__init__(directory)
        self._file += '/sound.dbf'
        self._primary_key = 'date'