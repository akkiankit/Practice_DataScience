# 8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'.

# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt

print("Welcome to Python Problem No 8.4 based on List")
path = "/Users/bigdaddy/Desktop/Python_Data_Science/CourseEra/PythonForEverybody/Course2PythonDataStructure/"
list1 = list()
fh = open(path + "mbox-short1.txt")
count = 0
for line in fh:
    line.strip()
    if line.startswith("From:"):
        line = line.split(" ")
        print(line[1].strip())
        count = count + 1

print("there are total ", count , "no of mail came from different")
