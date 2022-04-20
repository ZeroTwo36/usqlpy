class _BaseInsert:
    def __init__(self,**kwds):
        self.table = kwds.get("master")
        self.sqlmaster = kwds.get("sqlite_master",None)
        self.coll = kwds.get("collection",())

    def create(self):
        vals = ""
        for v in self.coll:
            vals += f'"{v}",'
        return f'INSERT INTO {self.table.name} VALUES ({vals[:-1]});'