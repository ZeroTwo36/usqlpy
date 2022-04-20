import json
from typing import Any, Iterable, List, Union
import requests
from .models import Table
from .glob import _BaseInsert

class SqlSession:
    def __init__(self,master) -> None:
        self.master = master
    
    def execute(self,code):
        response = requests.get(self.master.server_uri+"/usql",json={"sql":code},headers={
            "username":self.master.username,
            "password":self.master.password,
            "clustername":self.master.clusterdata.split("@")[0]
        })
        json = response.json()
        if "error" in json:
            print(f'Error: {json["error"]}')
            return []
        return json["result"]

class ItemStruct:
    def __init__(self,master):
        self.master = master
        self.items = {}

    def from_object(self,obj:Any):
        for item in list(obj.__dict__.keys()):
          if not item.startswith("__"):
            self.items[item] = obj.__dict__[item]

    def __getitem__(self,item):
        return self.items.get(item)
        
    def __setitem__(self,item,value):
        self.items[item] = value

class uSQLClient:
    def __init__(self,auth):
        self.auth = auth  #"usql+priscilla:anon:12345:cluster0@srv=priscilla"
        self.ns_proto, self.username, self.password, self.clusterdata = self.auth.split(":")
        self.server = self.ns_proto.split("+")[1]
        self.server_uri = f"https://{self.server}.usql.repl.co"
        self.session = SqlSession(self)
        self._session = self.session
        self.config = ItemStruct(self)

    def add(self,_mapping:Union[Table,_BaseInsert, List[_BaseInsert]]):
        if isinstance(_mapping, List):
          for _M in _mapping:
            for statement in _M.create().split(";"):
                self.session.execute(statement)
        else:
            for statement in _mapping.create().split(";"):
                self.session.execute(statement)