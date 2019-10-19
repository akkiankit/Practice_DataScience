# Matching and Extracting Data from web 

import re

x = 'my 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print(y)
y = re.findall('[AEIOU]+',x)
print(y)
#Greedy matching , Below example illustrates the greeding mathing concept
# ^F.+: where ^ represents the first character in the match is an F
# . represents any character
# + one or more time 
# : last character in the match is :

x = 'From using the : character'
y = re.findall('^F.+:',x)
print(y)

x = 'From using the : character ram:'
y = re.findall('^F.+:',x)
print(y)

# * and + , is used to greedy matching
#  ? is non greedy matching

st = 'From rjlowe@iupui.edu Fri Jan  4 14:50:18 2008'
st1 = re.findall('\S+@\S+',st)
print(st1)

st = 'From rjlowedfad@iupui.edu Fri Jan  4 14:50:18 2008'
st1 = re.findall('^From (\S+@\S+)',st)
print(st1)

