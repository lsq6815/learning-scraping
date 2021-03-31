#!/usr/bin/env python3
"""
use CSS Selector to find all name (tag with class green)
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup


def regularize(tag):
    """
    regularize input tag into reasonable str

    :param tag html-tag: tag inputed
    """
    result: str = tag.get_text().replace('\n', ' ').lower()
    # 去掉所有格
    if result.endswith("'s"):
        result = result[:-2]

    return result


# get html and convert into BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html.read(), features='lxml')

name_list = bsObj.select(".green")
name_list = map(regularize, name_list)

# convert into map, key is the name, value is the times the name shown
name_dict = {}
for item in name_list:
    name_dict[item] = name_dict.get(item, 0) + 1

# sort dict
# 1. show times of name (descent)
# 2. the length of name (ascent)
name_dict = dict(
    sorted(name_dict.items(), key=lambda i: (i[1], -len(i[0])), reverse=True))

for k, v in name_dict.items():
    print(f"#{v}: {k}")
