from typing import Iterable
from .glob import _BaseInsert

class Table:
    def __init__(self,name,columns=[]):
        self.columns = columns
        self.data = []
        self.name = name

    def add(self,__item__):
        self.columns.append(__item__)
        self.data.append(f'{__item__.name} {__item__.type}')

    def clear(self):
        self.columns = []
        self.data.clear()

    def create(self,drop:bool=False):
        name = self.name
        data = ',\n'.join(self.data)[:-1]
        
        if not not drop:
            totalStr = f"""
DROP TABLE IF EXISTS {name};\n
                """

            totalStr += f"""
CREATE TABLE {name}(
    {data}
);
            """
        else:
            totalStr = f"""        
CREATE TABLE {name}(
    {data}
);
            """

        return totalStr

    def insertone(self,entry:Iterable):
        return _BaseInsert(master=self,collection=entry)

    
    def insertmany(self,entries:Iterable[Iterable]):
        return [_BaseInsert(master=self,collection=entry) for entry in entries]



class Integer:
    def __init__(self,name):
        self.name = name
        self.type = "integer"
        
class Text:
    def __init__(self,name):
        self.type = "text"
        self.name = name

class Date:
    def __init__(self,name):
        self.type = "date"
        self.name = name
        