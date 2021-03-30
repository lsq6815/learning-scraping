#!/usr/bin/env python3
"""
use lambda in BeautifulSoup
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html.read(), features='lxml')

for tag in bsObj.find_all(lambda tag: len(tag.attrs) == 2):
    print(f"Tag: {tag.name}")
    for k, v in tag.attrs.items():
        if isinstance(v, list):
            print(f"{k}: ", end='')
            for i in v:
                print(i, end=' ')
            print('')
        else:
            print(f"{k}: {v}")
    print('')
