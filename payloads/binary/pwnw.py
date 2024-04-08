from core.challenge import Challenge
import logging

from utils.colors import Colors

import pwn

logging.getLogger("pwnlib").setLevel(logging.ERROR)

class Pwnw():
    def __init__(self, chall: Challenge):
        self.challenge = chall
        self.analyze()
    
    def analyze(self):
        for file in self.challenge.files:
            if "." not in file['name']:
                elf = pwn.ELF(file['path'])
                self.print_data(elf)
    
    def print_data(self, elf):
        if (elf.libc):
            non_libc = [symbol for symbol in elf.symbols if not elf.libc.symbols.get(symbol)]
        else:
            non_libc = elf.symbols
        print("{}SYMBOLS:{}".format(Colors.CYAN, Colors.END))
        for sym in non_libc:
            if not sym.startswith("__") and not sym.startswith("got.") and not sym.startswith("_") and "@" not in sym and "." not in sym:
                print("\t[{}{}{}] - {}".format(Colors.BLUE, hex(elf.symbols[sym]), Colors.END, sym))