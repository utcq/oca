import os
import requests
from config import *
from dumper import print_downloading

def get_files(files:list[str], cid:int)->list[dict]:
    dwnpath = "ocatmp/chall{}/".format(cid)
    try: 
        os.mkdir("ocatmp")
    except: pass
    try:
        os.mkdir(dwnpath)
    except: pass

    res = []
    
    for file in files:
        url = CONFIG['files'].format(
            file['url'].replace("/api/file/", "")
        )
        print_downloading(file['name'])
        r = requests.get(url)
        path = dwnpath+file['name']
        open(dwnpath+file['name'], "wb").write(r.content)
        res.append(
            {"name": file['name'], "path": path}
        )
    print("━"*24)
    return res