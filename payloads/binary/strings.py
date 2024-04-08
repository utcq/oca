from core.challenge import Challenge
import os

import logging
import pwn
logging.getLogger("pwnlib").setLevel(logging.ERROR)


class Strings():
    def __init__(self, chall: Challenge):
        self.challenge = chall
        self.analyze()
    
    def analyze(self):
        for file in self.challenge.files:
            if "." not in file['name']:
                elf = pwn.ELF(file['path'])
                res = os.popen("strings {}".format(file['path'])).read()
                for string in res.split("\n"):
                    if "/" not in string and "." not in string and not string.startswith("_") and len(string) > 3:
                        if (elf.libc):
                            if (not elf.libc.symbols.get(string)):
                                print(string)