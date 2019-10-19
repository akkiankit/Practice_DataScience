# Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py. 
# The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and 
# the other is the actual data you need to process for the assignment.
# Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_197650.html (Sum ends with 95)
# You do not need to save these files to your folder since your program will read the data directly from the URL. 
# Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.

import urllib.response,urllib.parse,urllib.error,urllib.request
from bs4 import BeautifulSoup
import ssl

# ignore the SSL certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("enter URL : ")
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_42.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
print("*****************************************************************************************")
# print( " title of the page : " ,soup.title)
# print("title name is : ", soup.title.name)
# print("title string is : ", soup.title.string)
# print("title parent name is ; ", soup.title.parent.name)
# print("p tag is ; ", soup.p)
# # print("soup.p['class'] is : ", soup.p['class'])
# print("anchor tag is ; ", soup.a)
# print("all a tag is : ", soup.find_all('a'))
# print("finding link name with index : ", soup.find(id="link3"))
# represents the document as a nested data structure:
# print(soup.prettify())
print("*****************************************************************************************")
# Retrieve all of the anchor tags
print("start of soup working")
tags = soup('a')
tags1 = soup('link')
for tag1 in tags1:
    print(tag1.get('href',None))

print("**************************************************")
for tag in tags:
    print(tag.get('href', None))
    # Look at the parts of a tag
    # print('TAG:', tag, "type of tag is : ", type(tag))
    # print('Contents:', tag.contents[0])
    # print('Attrs:', tag.attrs, "type is : ", type(tag.attrs))
    # print("############################################")

# First Method working fine 
# sum = 0
# for i in soup.find_all('span'):
#     sum = sum + int(i.get_text())
#     print(i.get_text())

# print(sum)




