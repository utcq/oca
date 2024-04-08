import requests
from bs4 import BeautifulSoup
from config import *
from files import get_files

from challenge import Challenge
from scraper.lil_parser import *

session = requests.Session()
BASE = CONFIG['base']
token = CONFIG['token']
headers = {
    "authorization": "Token {}".format(token)
}

def get_challenge(url:str)->Challenge:
    id = url.split("#")[1].split("-")[1]
    r = session.get(BASE.format(id), headers=headers)
    resp = r.json()
    return Challenge(
        name=resp['title'],
        url=url,
        id=id,
        categories=resp['tags'],
        score=resp['currentScore'],
        files=resp['files'],
        description=resp['description'],
        **parse_desc(resp['description'])
    )

def download_files(chall: Challenge)->None:
    chall.files = get_files(chall.files, chall.id)