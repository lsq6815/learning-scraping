#!/usr/bin/env python3
from urllib.request import urlopen
from bs4 import BeautifulSoup
try:
    html = urlopen("http://pythonscraping.com/pages/page1.html")
except HTTPError as e:
    # if encounter 404/500... etc.
    print(e)
    exit(0);

if html is None:
    # if URL is mistaken or page is not exist
    print("URL is not found")
    exit(0);

try:
    bad_content = bsObj.nonExistingTag.anotherTag
except AttributeError as e:
    # if the middle tag is non-exist
    print("Tag wasn't found")
    exit(0);

if bad_content is None:
    # if another tag isn't exist
    print("Tag wasn't found")

print(bad_content)
