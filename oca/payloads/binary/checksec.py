from core.challenge import Challenge
from utils.colors import Colors
import os

class Checksec():
    def __init__(self, chall: Challenge):
        self.challenge = chall
        self.analyze()
    
    def analyze(self)->None:
        for file in self.challenge.files:
            if "." not in file['name']:
                r = os.popen("checksec --format=json --file={}".format(file['path']))
                buff = r.read()
                if ("not found" not in buff.lower()):
                    data = eval(buff)[file['path']]
                    self.print_data(data)
    
    def print_data(self, data:dict)->None:
        print("{}RELRO: {}{}".format(
            Colors.CYAN,
            (Colors.RED if data['relro'] == 'no' else Colors.GREEN),
            data['relro'].capitalize()
        ))
        print("{}CANARY: {}{}".format(
            Colors.CYAN,
            (Colors.RED if data['canary'] == 'no' else Colors.GREEN),
            data['canary'].capitalize()
        ))
        print("{}NX: {}{}".format(
            Colors.CYAN,
            (Colors.RED if data['nx'] == 'no' else Colors.GREEN),
            data['nx'].capitalize()
        ))
        print("{}PIE: {}{}".format(
            Colors.CYAN,
            (Colors.RED if data['pie'] == 'no' else Colors.GREEN),
            data['pie'].capitalize()
        ))
        print("{}RPATH: {}{}{}".format(
            Colors.CYAN,
            (Colors.RED if data['rpath'] == 'no' else Colors.GREEN),
            data['rpath'].capitalize(),
            Colors.END
        ))