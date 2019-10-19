# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. 
# The program will prompt for a URL, read the XML data from that URL using urllib and then parse and 
# extract the comment counts from the XML data, compute the sum of the numbers in the file.

# We provide two files for this assignment. One is a sample file where 
# we give you the sum for your testing and the other is the actual data you need to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_197652.xml (Sum ends with 32)
# You do not need to save these files to your folder since your program will read the data directly from the URL. 
# Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
import urllib.request,urllib.response,urllib.parse,urllib.error
import ssl
import xml.etree.ElementTree as ET

data = input("enter the url or xml file details : ")
if len(data) < 1:
    data = "http://py4e-data.dr-chuck.net/comments_42.xml"

#ignore the certificate
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

stuff = urllib.request.urlopen(data, context=ctx).read()

content = ET.fromstring(stuff)
lst = content.findall("comments/comment")
sumitems = list()
for item in lst:
    # print(item.find('count').text)
    sumitems.append(int(item.find('count').text))

print(sumitems)
print(sum(sumitems))