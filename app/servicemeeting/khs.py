from app.lib.khs import KhsDataBase


class KhsDataServiceMeeting(KhsDataBase):
    def __init__(self, directory):
        super().__init__(directory)
        self._file += '/servicemeeting.dbf'
        self._primary_key = 'date'