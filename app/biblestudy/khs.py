from app.lib.khs import KhsDataBase


class KhsDataBibleStudy(KhsDataBase):
    def __init__(self, directory):
        super().__init__(directory)
        self._file += '/biblestudy.dbf'