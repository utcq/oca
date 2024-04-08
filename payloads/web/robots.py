from core.challenge import Challenge

import requests

class Robots():
    def __init__(self, chall: Challenge):
        self.challenge = chall
        self.analyze()

    def analyze(self):
        for url in self.challenge.urls:
            r = requests.get(url+"/robots.txt")
            res = r.content
            if (r.status_code==200):
                print(
                    '\n'.join([line.split(":")[-1].replace("*", "") for line in res.decode().split("\n")]).strip().replace(" /", "/")
                )