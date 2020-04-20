from tkinter import *
from tkinter.messagebox import *

fen=Tk()
# les fonctions...........
def valider(*args):
    vs3.set(vs1.get()+vs2.get())
    showinfo(vs1.get())


def effacer():
    lib4.set("fffffffffffff")

def valider2(*args):
    chn = str(vs1.get())+" + "+ str(vs2.get())+ " résultat= "+str(vs3.get())
    lib4.config(text = chn)

def effacer(*args):
    vs1.set(0)
    vs2.set(0)
    lib4.config(text="")
    lib3.config(text="")
# les libélles


lib1=Label(fen,text="Donner le premier entier :")
lib1.grid(row=1,column=1,padx=10,sticky="E")
lib2=Label(fen,text="Donner le deuxiéme entier:")
lib2.grid(row=2,column=1,padx=10,sticky="E")
lib3=Label(fen,text="Resultat=").grid(row=3,column=1)
lib4=Label(fen,text="résultat=")
lib4.grid(row=4,column=1)


 # les champs des saisies
vs1=IntVar()
s1=Entry(fen,text="valeur 1",textvariable=vs1).grid(row=1,column=2)
vs2=IntVar()
s2=Entry(fen,text="valeur 2",textvariable=vs2).grid(row=2,column=2)
vs3=IntVar()
s2=Entry(fen,text="",textvariable=vs3).grid(row=3,column=2)

# le cannevas et son image (232x245)
cannevasImg = Canvas (fen, width =245, height = 258, bg = "green")
photo1 = PhotoImage (file="2292.png")
image1 = cannevasImg.create_image(124, 131, image = photo1)
cannevasImg.grid(row = 1, column = 4, rowspan = 4, padx = 10, pady = 10)

cannevasImg1 = Canvas (fen, width =245, height = 258, bg = "dark green")
photo2= PhotoImage (file="2485.png")
image2 = cannevasImg1.create_image(124, 131, image = photo2)
cannevasImg1.grid(row = 1, column = 5, rowspan = 4, padx = 10, pady = 10)

# les boutons.............
photo3 = PhotoImage (file="2292.png")
b1=Button(fen,text="Valider",image=photo3,command=valider).grid(row=5,column=1)
b2=Button(fen,text="Valider2",command=valider2).grid(row=5,column=2)
b2=Button(fen,text="effacer",command=effacer).grid(row=5,column=3)
b3=Button(fen,text="Quiter",command=fen.quit).grid(row=5,column=4)

fen.mainloop() # boucle de capture des événements
fen.destroy() # fin de l'application


