# Following Links in Python

# In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. 
# The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, 
# scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times 
# and report the last name you find.

# We provide two files for this assignment. 
# One is a sample file where we give you the name for your testing and 
# the other is the actual data you need to process for the assignment

# Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
# Last name in sequence: Anayah
# Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Aine.html
# Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. 
# The answer is the last name that you retrieve.
# Hint: The first character of the name of the last page that you will load is: S

import urllib.request,urllib.response,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("enter url: ")

if len(url) < 1 :
    url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"

count = 0

while count < 7:
    # print("start of while loop")
    # print(url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    cnt = 0
    for tag in tags:
        cnt = cnt + 1
        if cnt == 18 :
            url = tag.get('href', None)
            # print(tag.get('href', None))
            print("***********", tag.contents[0], "*************")
            break

    count = count + 1






    
    # # <li style="margin-top: 75px;"><a href="http://py4e-data.dr-chuck.net/known_by_Annalise.html">Annalise</a></li>
    # print(tag.contents[0])
    # # output <a href="http://py4e-data.dr-chuck.net/known_by_Amyleigh.html">Amyleigh</a>
    # print(tag.attrs.get('href',None))
    # print("***********************")




