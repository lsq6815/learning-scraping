#!/usr/bin/env python3
from urllib.request import urlopen

"""
urlopen return urllib.response.addinfourl

urllib.response define file-like interface like `read()` and `readline()`
urllib.response.addinfourl add additional attributes like url, headers and status
"""
html = urlopen("http://pythonscraping.com/pages/page1.html")
print(
    f"URL: {html.url}",
    f"status: {html.status}",
    f"headers: {html.headers}",
    f"###body###\n{html.read().decode('utf-8')}\n###body###",
    sep='\n')
