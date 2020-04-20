from tkinter import *
from tkinter.messagebox import *
from sqlite3 import *
#import sqlite3

# connection
con1=connect("base1.db")

cur1=con1.cursor()
my_name=("Ali",)
cur1.execute('SELECT * FROM personne WHERE nom= ?',my_name)
print(f"le nom d'utlisateur est : {cur1.fetchone()[1]}")


con1.close()




