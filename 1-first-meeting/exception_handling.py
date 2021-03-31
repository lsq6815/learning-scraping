#!/usr/bin/env python3
"""
如何处理获取和解析HTML时的错误
"""

from urllib.error import HTTPError
from urllib.request import urlopen

from bs4 import BeautifulSoup

try:
    html = urlopen("http://pythonscraping.com/pages/page1.html")
except HTTPError as e:
    # 如果遭遇404，500…… 这样的错误
    print(e)
    exit(0)

if html is None:
    # 如果URL写错了或者网页不存在了
    print("URL is not found")
    exit(0)

try:
    bsObj = BeautifulSoup(html.read(), 'lxml')
    content = bsObj.middleTag.tailTag
except AttributeError as e:
    # 如果中间的tag是不存在的
    print("middleTag wasn't exist")
    exit(0)

if content is None:
    # 如果尾标签不存在
    print("tailTag wasn't found")

print(content)
