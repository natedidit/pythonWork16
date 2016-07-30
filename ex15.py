# Student: Nate Canney
# Programming Exercise: 15

from tkinter import *
import mysql.connector

conn = mysql.connector.connect(user='tcm159', password='sGkY4651',
host='localhost', database='customers')

qry = conn.cursor()

qry.execute("SELECT * FROM campus")

tbl = qry.fetchall()

s = "Results:\n"

if len(tbl) > 0:
    for row in tbl:
        s += row[0] + " " + row[1] + " " + row[2] + "\n"
else:
    s = "Not record found."
conn.close()

root = Tk()

root.title('Message Box')
Label(root, justify=LEFT, text=s).grid()

root.mainloop()
