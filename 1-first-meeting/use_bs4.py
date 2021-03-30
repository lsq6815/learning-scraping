#!/usr/bin/env python3
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html.read(), features='lxml')
# same as 
# bsObj.html.body.h1
# bsObj.body.h1
# bsObj.html.h1
print(bsObj.h1)
