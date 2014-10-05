from app.lib.khs import KhsDataBase


class KhsDataOutlines(KhsDataBase):
    def __init__(self, directory):
        super().__init__(directory)
        self._file += '/outlines.dbf'
        self._primary_key = 'outline'