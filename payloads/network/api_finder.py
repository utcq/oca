from core.challenge import Challenge
from utils.colors import Colors

import pyshark

class Api_finder():
    def __init__(self, chall: Challenge):
        self.challenge = chall
        self.filter='http.request.uri contains "api" || http.request.uri contains "debug"'
        
        self.analyze()
    
    def analyze(self):
        for file in self.challenge.files:
            if ".pcapng" in file['name']:
                self.finder(file['path'])
    
    def finder(self, path:str):
        cap = pyshark.FileCapture(path, display_filter=self.filter)
        if not len(list(cap)):
            print("{}[SHARK] {}No API found{}".format(Colors.CYAN, Colors.RED, Colors.END))
            return
        
        for packet in cap:
            print("{}[SHARK] {}Exposed {}'{}'{}".format(
                Colors.CYAN, Colors.GREEN, Colors.BLUE,
                packet.http.request_uri, Colors.END
            ))
