fname = input("enter file name you want to read: ")

path = "/Users/bigdaddy/Desktop/Python_Data_Science/CourseEra/PythonForEverybody/Course2PythonDataStructure/"
print('file path is : ',path)
try:
    filecontent = open(path + fname)
except:
    con = input("wrong file name entered: if you want to continue press Y or N : ")
    print(con)
    if con.upper() == "Y":
        fname = input("enter file name you want to read: ")
    else:
        quit()    

for line in filecontent:
    line = line.rstrip()
    print(line.upper())
