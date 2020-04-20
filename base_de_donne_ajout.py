from tkinter import *
from tkinter.messagebox import *
from sqlite3 import *
#import sqlite3

# connection
con1=connect("base1.db")

cur1=con1.cursor()
nper=(cur1.lastrowid,"Habiba","boubaker")
cur1.execute('INSERT INTO personne VALUES (?,?,?)',nper)
con1.commit()
print("nouveau utilisateur ajouté............")

con1.close()




