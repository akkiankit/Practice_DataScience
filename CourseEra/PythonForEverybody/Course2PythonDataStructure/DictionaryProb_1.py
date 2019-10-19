# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

fname = input("enter file name : ")
path = "/Users/bigdaddy/Desktop/Python_Data_Science/CourseEra/PythonForEverybody/Course2PythonDataStructure/"
list1 = list()
dict1 = dict()
try:
    if len(fname) < 1 :
        fname = "mbox-short1"

    fh = open(path + fname + ".txt")
except:
    print("not found")
    quit()

for line in fh:
    if line.startswith("From:"):
        words = line.split(" ")
        for word in words:
            if word == "From:":
                list1.append(words[1].rstrip())

for listval in list1:
    #Below line works as if the key exists then add else if it doesnot exists then 
    #by default it return 0
    # for example dict1[item] = dict1.get(item,0) + 1 
    # here item i.e if not exists in dict then it will be 0 by default but if it exist then 0 won't be default?
    dict1[listval] = dict1.get(listval,0) + 1
bigcount = None
bigword = None
for k,v in dict1.items():
    if (bigcount is None) or (v > bigcount):
        bigword = k
        bigcount = v


print(bigword,bigcount)