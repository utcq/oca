import requests
from bs4 import BeautifulSoup
from utils.config import *
import regex as re

from core.challenge import Challenge


class Scraper():
    def __init__(self, url:str):
        self.url = url
        self.session = requests.Session()
        self.base = CONFIG['base']
        self.token = CONFIG['token']
        self.headers ={
            "authorization": "Token {}".format(self.token)
        }
    
    def get_challenge(self)->Challenge:
        id = self.url.split("#")[1].split("-")[1]
        r = self.session.get(self.base.format(id), headers=self.headers)
        resp = r.json()

        try:
            return Challenge(
                name=resp['title'],
                url=self.url,
                id=id,
                categories=resp['tags'],
                score=resp['currentScore'],
                files=resp['files'],
                description=resp['description'],
                **self.parse_desc(resp['description'])
            )
        except:
            raise EnvironmentError("Invalid Authentication Token")
        
    
    def parse_desc(self, desc:str)->dict:
        res = {
            "urls": [],
            "hosts": []
        }

        regex_pattern = r"\bhttps?://(?![\[\(])\S+\b"
        matches=re.findall(regex_pattern, desc, re.MULTILINE | re.DOTALL)
        for match in matches:
            if "]" in match:
                match = match.split("]")[0]
            res["urls"].append(
                match
            )
    
        regex_pattern = r"nc [a-zA-Z0-9\-_]+(?:\.challs\.olicyber\.it) \d+"
        matches=re.findall(regex_pattern, desc, re.MULTILINE | re.DOTALL)
        for match in matches:
            res["hosts"].append(
                tuple(match.split("nc ")[1].split(" "))
            )

        return res