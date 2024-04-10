from core.challenge import Challenge
from utils.colors import Colors
import os

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
            os.system("cd {}; pwninit --bin {}{}{}".format(
                binary["path"],
                " --ld {}".format(linker["name"]) if linker!=None else "",
                " --libc {}".format(libc["name"]) if libc!=None else ""
            ))


        
