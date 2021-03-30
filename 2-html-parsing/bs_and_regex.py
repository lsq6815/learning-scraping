#!/usr/bin/env python3
"""
use regex with BeautifulSoup
"""
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html.read(), features='lxml')
images = bsObj.find_all("img", {"src": re.compile(r"gifts/img\d+")})
for image in images:
    # to get all attrs in dict: image.attrs
    print(image['src'])
