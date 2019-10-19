# Finding Numbers in a Haystack
# In this assignment you will read through and parse a file with text and numbers. 
# You will extract all the numbers in the file and compute the sum of the numbers.
# Data Files
# We provide two files for this assignment. One is a sample file where we give you 
# the sum for your testing and the other is the actual data you need to process for the assignment.
# Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
# Actual data: http://py4e-data.dr-chuck.net/regex_sum_197648.txt (There are 83 values and the sum ends with 8)
# These links open in a new window. Make sure to save the file into the same folder as you will be writing your Python program. 
# Note: Each student will have a distinct data file for the assignment - so only use your own data file for analysis.

import re
path = "/Users/bigdaddy/Desktop/Python_Data_Science/CourseEra/PythonForEverybody/Course3PythonToAccessWebData/"

fname = input("enter file name : ")
try:
    if len(fname) < 1 : 
        fname = "regex_sum_42.txt"
    
    fh = open(path + fname )
except:
    print("file not found")
    quit()

list1 = list()
for line in fh:
    # print(line)
    line.strip()
    number = re.findall('[0-9]+',line)

    if len(number) < 1:
        continue
    for num in number:
        list1.append(num)
    
print(list1)
sum = 0

for s in list1:
    sum = sum + int(s)

print("sum is : " , sum)
    # words = line.split()
    # for word in words:
    #     if re.findall('[0-9]+',word):
    #         print(word)