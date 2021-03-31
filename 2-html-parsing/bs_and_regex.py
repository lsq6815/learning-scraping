#!/usr/bin/env python3
"""
use regex with BeautifulSoup
"""
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html.read(), features='lxml')

# BeautifulSoup 执行的是search（找子串）而不是match（匹配串），不用写全
images = bsObj.find_all("img", {"src": re.compile(r"gifts/img\d+")})
for image in images:
    # to get all attrs in dict: image.attrs
    print(image['src'])
