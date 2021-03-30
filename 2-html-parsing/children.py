#!/usr/bin/env python3
"""
get tag's children tags
"""
from urllib.request import urlopen
import bs4
from bs4 import BeautifulSoup

from gift import Gift

def tag2gift(tag: bs4.element.Tag):
    """
    extrace info from tag and return the Gift Object constructed by those info

    :param tag bs4.element.Tag: html tag
    """
    name: str = tag.select_one("td:first-child").get_text().strip()
    description: str = tag.select_one("td:nth-child(2)").get_text().strip()
    price_str: str = tag.select_one("td:nth-child(3)").get_text().strip()
    price: float = float(price_str[1:].replace(',', ''))

    return Gift(name, description, price)


html = urlopen("http://pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html.read(), features='lxml')

# for child in bsObj.select("table#giftList > tr.gift"):
#     gifts.append(tag2gift(child))
gifts = map(tag2gift, bsObj.select("table#giftList > tr.gift"))

for gift in sorted(gifts, key=lambda i: (-i.price, len(i.name)) ):
    print(gift)
