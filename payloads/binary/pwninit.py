from core.challenge import Challenge
from utils.colors import Colors
import os,sys

class Pwninit:
    def __init__(self, chall: Challenge):
        r = os.system("pwninit -V >> /dev/null")
        if(r!=0):
            print("{}Error{}: Pwninit is not installed".format(Colors.RED, Colors.END))
            return
        
        r = os.system("patchelf --version >> /dev/null")
        if(r!=0):
            print("{}Error{}: Patchelf is not installed".format(Colors.RED, Colors.END))
            return
        
        self.challenge = chall
        self.writesolve()
    
    def writesolve(self):
        binary = None
        linker = None
        libc = None
        for file in self.challenge.files:
            if "." not in file["name"]:
                binary=file
            elif "ld" in file["name"]:
                linker=file
            elif "libc" in file["name"]:
                libc=file
        
        r = os.popen("file {}".format(binary["path"]))
        if "executable" not in r.read():
            print("{}Error{}: no executable found".format(Colors.RED, Colors.END))
        else:
            try: os.remove("ocatmp/chall{}/solve.py".format(self.challenge.id))
            except: pass
            r = os.popen("cd {}; pwninit --bin {}{}{}".format(
                "ocatmp/chall{}/".format(self.challenge.id),
                binary["path"].replace("ocatmp/chall{}/".format(self.challenge.id), ""),
                " --ld {}".format(linker["name"]) if linker!=None else "",
                " --libc {}".format(libc["name"]) if libc!=None else ""
            )).read()
            os.system("mv {} {}".format(binary["path"]+"_patched", binary["path"]))
            print(r)
            
            filez = open("ocatmp/chall{}/solve.py".format(self.challenge.id), "rb")
            cont = filez.read().decode().replace(
                binary["path"].replace("ocatmp/chall{}/".format(self.challenge.id), "")+"_patched",
                binary["path"]
            )
            if len(self.challenge.hosts):
                cont = cont.replace('("addr", 1337)',
                     '("{}", {})'.format(*self.challenge.hosts[0])
                    )
            file = open("ocatmp/chall{}/solve.py".format(self.challenge.id), "w")
            file.write(cont)

            file.close()
            sys.stdout.flush()
            print("Run solve with './{} LOCAL'".format("ocatmp/chall{}/solve.py".format(self.challenge.id)))


        
