from tkinter import *
from tkinter.messagebox import *
from sqlite3 import *
#import sqlite3

# connection
try:
    con1=connect("base1.db")

    cur1=con1.cursor()
    req1=cur1.execute('SELECT * FROM personne')
    print("nom       !    prenom")
    print(' -------------------- !')
    for row in req1.fetchall():
        print(f"! {row[1]}  !   {row[2]} !")
except Exception as e:
    #****
    print("[ERREUR]")
    con1.rollback()
finally:
    con1.close()




