# #object orieted Programming 
# a program is made up of many cooperating objects
# instead of being the whole program - each object is a little "island" within the program and cooperatively working with other objects 
# A program is made up of one or more objects working together -objects make use of each othere's capabilities

# what is object 
# An object is a bit of self -contained code and  Data
# A key aspect of the object approach is to break the problem into smaller understandable parts (divide and conquer)
# Objects have boundaries that  allow us to ignore un-needed details
# We have been using objects all along : string Objects,Integer objects, Dictionary Onjects,List Objects...
import sqlite3

#connection set up to emaildb.sqlite, if the file doesnot exists then 
# it will create one new one 
conn = sqlite3.connect('/Users/bigdaddy/Desktop/Python_Data_Science/CourseEra/PythonForEverybody/Course4DatabasewithPython/emaildb.sqlite')
#icursor ts kind of handle
cur = conn.cursor()


cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (email Text, count INTEGER)''')
path = "/Users/bigdaddy/Desktop/Python_Data_Science/CourseEra/PythonForEverybody/Course2PythonDataStructure/"
fname = input('enter file name: ')
if (len(fname) < 1):
    fname = 'mbox-short.txt'
fh = open(path + fname)

for line in fh:
    if not line.startswith('From: '):
        continue
    piece = line.split()
    email = piece[1]
    #it is kind like dictionary object
    # ? = is place holder
    cur.execute('SELECT count FROM Counts WHERE email=?', (email,))
    row = cur.fetchone()
    if row is None:

        cur.execute('''INSERT INTO Counts (email, count) VALUES (?,1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count +1 WHERE email = ?', (email,))

    conn.commit()   
    # print(email)
#https
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]),row[1])

cur.close