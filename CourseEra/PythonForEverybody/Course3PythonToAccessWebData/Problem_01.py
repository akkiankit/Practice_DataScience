#Regular Expression 
import re


fname = input("enter file name : ")
path = "/Users/bigdaddy/Desktop/Python_Data_Science/CourseEra/PythonForEverybody/Course2PythonDataStructure/"

try:
    if len(fname) < 1 :
        fname = "mbox-short1.txt"
    
    fh = open(path + fname )
except:
    print("No file found ")

for line in fh:
    if re.search('From ', line):
        print(line.rstrip())