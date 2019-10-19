# 8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. 
# The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. 
# When the program completes, sort and print the resulting words in alphabetical order.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt
print("Welcome to Python Problem No 8.4 based on List")
path = "/Users/bigdaddy/Desktop/Python_Data_Science/CourseEra/PythonForEverybody/Course2PythonDataStructure/"
list1 = list()
fh = open(path + "romeo.txt")
for line in fh:
    word = line.split()
    for wd in word:
        list1.append(wd)

list1.sort()

for i in list1:
    count = list1.count(i)
    if count > 1:
        list1.remove(i)

print(list1)


