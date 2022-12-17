import mysql.connector as sqc
'''
con = sqc.connect(host="localhost", user="root", passwd="toor")
cur = con.cursor()
cur.execute("CREATE DATABASE school")

con = sqc.connect(host="localhost", user="root", passwd="toor", db = "school")
cur = con.cursor()
cur.execute("CREATE TABLE student_detail(rollno INT NOT NULL PRIMARY KEY, name VARCHAR(255) NOT NULL, class VARCHAR(10))")
cur.execute("CREATE TABLE student_marks(rollno INT NOT NULL PRIMARY KEY, overallmarks VARCHAR(5))")
'''

'''
con = sqc.connect(host="localhost", user="root", passwd="toor", db = "school")
cur = con.cursor()

cur.execute("SELECT * FROM student_detail")
r = cur.fetchall()
for i in r:
    print(i)
'''

'''
def recSec(rno):
    con = sqc.connect(host="localhost", user="root", passwd="toor", db = "school")
    cur = con.cursor()
    cur.execute("select rollno from student_detail")
    r = cur.fetchall()
    found = False
    for i in r:
        if rno == i[0]:
            found = True
            break

    if found:
        return "EXISTS"
    else:
        return "DOES NOT EXIST"

x = int(input("Enter roll no to search: "))

print(f"The record for roll no. {x}, {recSec(x)}.")
'''

'''
con = sqc.connect(host="localhost", user="root", passwd="toor", db = "school")
cur = con.cursor()

rno = int(input("Enter Roll No. you want to delete: "))

syn = f"DELETE FROM student_detail WHERE rollno = {rno}"
cur.execute(syn)
con.commit()
cur.execute("SELECT name FROM student_detail ORDER BY name ASC")
for i in cur.fetchall():
    print(i[0])

'''