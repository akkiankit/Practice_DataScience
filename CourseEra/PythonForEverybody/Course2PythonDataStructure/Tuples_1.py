# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fname = input("enter the file name : ")
path = "/Users/bigdaddy/Desktop/Python_Data_Science/CourseEra/PythonForEverybody/Course2PythonDataStructure/"

try:
    if len(fname) < 1 : 
        fname = "mbox-short1.txt"
    fh = open(path + fname )
except:
    print("File not found")
    quit()

list1 = list()
for line in fh:
    if line.startswith("From "):
        words = line.split()
        hrs = words[5].split(":")
        list1.append(hrs[0])

dict1 = dict()
list1.sort()
for item in list1:
    dict1[item] = dict1.get(item,0) + 1

for k,v in dict1.items():
    print(k,v)
       
