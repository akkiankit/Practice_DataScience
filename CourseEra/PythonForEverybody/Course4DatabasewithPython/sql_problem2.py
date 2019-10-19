# Counting Organizations
# This application will read the mailbox data (mbox.txt) and count the number of email messages per organization 
# (i.e. domain name of the email address) using a database with the following schema to maintain the counts.
# CREATE TABLE Counts (org TEXT, count INTEGER)
# When you have run the program on mbox.txt upload the resulting database file above for grading.
# If you run the program multiple times in testing or with dfferent files, make sure to empty out the data before each run.
# You can use this code as a starting point for your application: http://www.py4e.com/code3/emaildb.py.
# The data file for this application is the same as in previous assignments: http://www.py4e.com/code3/mbox.txt.
# Because the sample code is using an UPDATE statement and committing the results to the database as each record is read in the loop, 
# it might take as long as a few minutes to process all the data. The commit insists on completely writing all the data to disk every time it is called.
# The program can be speeded up greatly by moving the commit operation outside of the loop. In any database program, 
# there is a balance between the number of operations you execute between commits and the importance of not losing the results of 
# operations that have not yet been committed.

import sqlite3

conn = sqlite3.connect("/Users/bigdaddy/Desktop/Python_Data_Science/CourseEra/PythonForEverybody/Course4DatabasewithPython/db1.sqlite")
cur = conn.cursor()
cur.execute(''' drop table if exists Counts''')
cur.execute(''' CREATE TABLE Counts (org TEXT, count INTEGER)''')
path = "/Users/bigdaddy/Desktop/Python_Data_Science/CourseEra/PythonForEverybody/Course4DatabasewithPython/"
fname = input('enter file name ; ')
if len(fname) < 1:
    fname = "mbox.txt"
fh = open(path + fname)
dic = dict()
for line in fh:
    if line.startswith("From "):
        words= line.split()
        domainNames = words[1].split("@")
        orgname = domainNames[1]
        cur.execute('select count from Counts where org = ?', (orgname,))
        row = cur.fetchone()
        if row is None:
            cur.execute('insert into Counts (org, count) values(?,1)',(orgname,))
        else:
            cur.execute('update Counts set count = count + 1 where org=?',(orgname,))
        # dic[domainNames[1]] = dic.get(domainNames[1],0) + 1

conn.commit()  

sqlstr = '''select org, count from Counts where count = (select max(count) from Counts)'''

for row in cur.execute(sqlstr):
    print(row)




# print(dic)
    