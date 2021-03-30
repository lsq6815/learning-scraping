#!/usr/bin/env python3
"""
use lxml's xpath to find all name (tag with class green)
"""

from urllib.request import urlopen
from lxml import etree


def regularize(name: str):
    """
    regularize input name into reasonable format

    :param name: name of novel characters
    """
    result: str = name.replace('\n', ' ').lower()
    # 去掉所有格
    if result.endswith("'s"):
        result = result[:-2]

    return result


# get html and convert into BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
xml = etree.HTML(html.read())

# text() is built-in function to extract tag content
name_list = xml.xpath('//*[@class="green"]/text()')
print(f"{name_list=}")
name_list = map(regularize, name_list)

# convert into map, key is the name, value is the times the name shown
name_dict = {}
for item in name_list:
    name_dict[item] = name_dict.get(item, 0) + 1

# sort dict
# 1. show times of name (descent)
# 2. the lenght of name (asecent)
name_dict = dict(
    sorted(name_dict.items(), key=lambda i: (i[1], -len(i[0])), reverse=True))

for k, v in name_dict.items():
    print(f"#{v}: {k}")
