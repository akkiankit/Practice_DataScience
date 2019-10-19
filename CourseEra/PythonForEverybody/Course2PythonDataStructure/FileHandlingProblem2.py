print("welcome to python data structure problem 7.2")
path = "/Users/bigdaddy/Desktop/Python_Data_Science/CourseEra/PythonForEverybody/Course2PythonDataStructure/"
Flag = True
count = 0
sum = 0
while Flag:
    try:
        # fname = input("enter file name to read: ")
        
        # fh = open(path + fname + ".txt")
        fh = open(path  + "mbox-short.txt")
        Flag = False
    except:
        print("not found ")
        val = input("you want to contnuie with other file name enter Y if want to contnuie else N: ")
        if val.upper() == "Y":
            print("wrong file name, enter again : ")
            continue
        else:
            quit()    

for line in fh:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence: "):
        count = count + 1
        lineSplit = line.split(":")
        decimal_part = lineSplit[1].strip()
        sum = sum + float(decimal_part)


   
print("Total no of line starting with x -dspam : ", count, "avg is : ", sum/count)
print(sum)