#!/usr/bin/env python3
"""
Hello BeautifulSoup
"""

from urllib.request import urlopen

from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html.read(), features='lxml')
# 下面的语句等价于
# print(bsObj.html.body.h1)
# print(bsObj.body.h1)
# print(bsObj.html.h1)
print(bsObj.h1)
