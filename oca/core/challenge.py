import os
import requests
from utils.config import *
from utils.colors import Colors

class Challenge:
    def __init__(
                self, name:str="", url:str="", score:int=0, id:int=0,
                categories:list[str]=[],
                urls:list[str]=[], files:list[dict]=[], hosts:list[tuple[str,int]]=[],
                writeup:str="", description:str=""
                ):
        self.name=name
        self.score=score
        self.id=id
        self.url=url
        self.categories=categories
        self.urls=urls
        self.files=files
        self.hosts=hosts
        self.writeup=writeup
        self.description=description
    
    def get_files(self)->list[dict]:
        dwnpath = "ocatmp/chall{}/".format(self.id)
        try: 
            os.mkdir("ocatmp")
        except: pass
        try:
            os.mkdir(dwnpath)
        except: pass

        res = []
        
        for file in self.files:
            url = CONFIG['files'].format(
                file['url'].replace("/api/file/", "")
            )
            print("{}[FILE] {}Downloading {}{}{}".format(Colors.CYAN, Colors.RED, Colors.CYAN, file['name'], Colors.END))
            r = requests.get(url)
            path = dwnpath+file['name']
            open(dwnpath+file['name'], "wb").write(r.content)
            res.append(
                {"name": file['name'], "path": path}
            )
        print("━"*24)
        self.files=res