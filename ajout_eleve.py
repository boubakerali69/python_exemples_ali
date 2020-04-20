from tkinter import *
from tkinter.messagebox import *
from sqlite3 import *

def ajout_eleve(*args):
    con1=connect("base1.db")
    cur1=con1.cursor()
    print(vnom.get()+"----"+vprenom.get())
    nel=(cur1.lastrowid,vnom.get(),vprenom.get(),vadresse.get(),vmoyenne.get())

    cur1.execute('INSERT INTO eleves VALUES (?,?,?,?,?)',nel)

    print("Ajout effectué ...............")
    con1.commit()
    con1.close()
def rech_eleve(*args):
    con1=connect("base1.db")
    cur1=con1.cursor()
    rech1=(vnom.get(),vprenom.get())
    cur1.execute('SELECT * FROM eleves WHERE nom_el=? AND prenom_el=?',rech1)
    resultat=cur1.fetchall()
    for el in resultat:
        print(el)
"""
    resultat=cur1.fetchone()
    while resultat:
        print(resultat)
        resultat=cur1.fetchone()


"""

#creation fentre dev saisie
fen1=Tk()
fen1.geometry("600x500")

lib1=Label(fen1,text="Saisie les données d'un élève").place(x=100,y=10)
# libelles des saisies
lib2=Label(fen1,text="Nom éléve :").place(x=20,y=50)
lib3=Label(fen1,text="Prénom éléve :").place(x=20,y=100)
lib4=Label(fen1,text="Adresse éléve :").place(x=20,y=150)
lib5=Label(fen1,text="Moyenne éléve :").place(x=20,y=200)
# les champs des saisies
vnom=StringVar()
snom=Entry(fen1,text="nom",textvariable=vnom).place(x=120,y=50)

vprenom=StringVar()
sprenom=Entry(fen1,text="Prenom",textvariable=vprenom).place(x=120,y=100)

vadresse=StringVar()
sadresse=Entry(fen1,text="Adresse",textvariable=vadresse).place(x=120,y=150)

vmoyenne=DoubleVar()
smoyenne=Entry(fen1,textvariable=vmoyenne).place(x=120,y=200)

# les boutons
bajout=Button(fen1,text="Ajout",command=ajout_eleve).place(x=20,y=350)
brecherche=Button(fen1,text="Recherche",command=rech_eleve).place(x=100,y=350)
bexit=Button(fen1,text="Exit",command=fen1.destroy).place(x=300,y=350)



fen1.mainloop() # boucle de capture des événements
#fen1.destroy() # fin de l'application