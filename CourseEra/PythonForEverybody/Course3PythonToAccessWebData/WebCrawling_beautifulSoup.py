import urllib.response,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore the SSL certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("enter the url : ")
#Below line of code is used to read whole page of url, Basically it returns a big string
html = urllib.request.urlopen(url, context=ctx).read()
# Below line of code is used to creat a soup object where it will parse all the strings stored in html variable.
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all the anchor tag from web pages.
tags = soup('a')
for tag in tags:
    print(tag.get('href',None))
