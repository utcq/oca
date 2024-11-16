import os
import requests
from utils.config import *
from utils.colors import Colors
from zipfile import ZipFile 

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
        self.path=""

    def __map_dir(self, path:str)->list[str]:
        file_map = {}
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                file_map[file] = file_path
        return file_map
    
    def resolve_tags(self):
        if "aliases" in CONFIG.keys():
            newtags = []
            for tag in self.categories:
                found = False
                for base_tag in CONFIG["aliases"]:
                    if tag in CONFIG["aliases"][base_tag] and base_tag not in newtags:
                        newtags.append(base_tag)
                if not found:
                    newtags.append(tag)
            self.categories = newtags

    
    def get_files(self)->list[dict]:
        self.path = "ocatmp/chall{}/".format(self.id)
        try: 
            os.mkdir("ocatmp")
        except: pass
        try:
            os.mkdir(self.path)
        except: pass
        res = []
        for file in self.files:
            url = CONFIG['files'].format(
                file['url'].replace("/api/file/", "")
            )
            print("{}[FILE] {}Downloading {}{}{}".format(Colors.CYAN, Colors.RED, Colors.CYAN, file['name'], Colors.END))
            r = requests.get(url)
            path = self.path+file['name']
            open(self.path+file['name'], "wb").write(r.content)
            if path.endswith(".zip"):
                print("{}[ARCHIVE] {}Uncompressing {}{}{}".format(Colors.CYAN, Colors.RED, Colors.CYAN, file['name'], Colors.END))
                with ZipFile(path, 'r') as zobject:
                    zobject.extractall(path=self.path)
                res = []
                file_map = self.__map_dir(self.path)
                for file in file_map:
                    res.append(
                        {"name": file, "path": file_map[file]}
                    )
            else:
                res.append(
                    {"name": file['name'], "path": path}
                )
        print("━"*24)
        self.files=res