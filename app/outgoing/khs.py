from app.lib.khs import KhsDataBase


class KhsDataOutgoing(KhsDataBase):
    def __init__(self, directory):
        super().__init__(directory)
        self._file += '/outgoing.dbf'
        self._remap_fields = {'congregati':'congregation'}