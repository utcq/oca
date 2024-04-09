from elftools.elf.elffile import ELFFile
from elftools.elf.sections import SymbolTableSection
import struct

from core.challenge import Challenge
from utils.colors import Colors

class Stack_frame():
    def __init__(self, chall: Challenge):
        self.challenge = chall
        self.analyze()
    
    def analyze(self):
        pass