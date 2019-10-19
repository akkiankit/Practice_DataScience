import urllib.request,urllib.parse,urllib.error

# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')

print("*****************************start copy from here *******************************")
for line in fhand:
    print(line.decode())

print("&&&&&&&&&&&&&&&&&&copy till here &&&&&&&&&&&&&&&&&&&&&&###########################")