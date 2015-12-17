from app.lib.khs import KhsDataBase


class KhsDataOCLM(KhsDataBase):
    def __init__(self, directory):
        super().__init__(directory)
        self._file += '/oclm.dbf'
        self._primary_key = 'date'