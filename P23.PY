from tkinter import *
from os import *

def effacer_ecran():
    system("cls")

def afficher(event):
    print("La touche [A] a été pressé")

def afficher1(event):
    print("Le bouton clic gauche été pressé")
def quitter():
    exit()
def escape(event):
    event.widget.destroy()
    print("{} -  {}  -  {}".format(event.keysym,event.keycode,event.x))
    print("fermeture fénêtre 2........")


def ouverture1():
    fen2=Toplevel()
    fen2.geometry("200x200")
    lib1=Label(fen2,text="Deuxième fenêtre")
    fen2.bind('<Escape>',escape)
    lib1.pack()



fen=Tk()
fen.title("Mon premier programme")
#fen.minsize(600,300)
#fen.maxsize(900,600)
fen.geometry("600x400+250+50")
lib1=Label(fen,text="Fiche client")
lib1.place(x=50,y=20)



s1=Entry(fen)
#s1.bind('<a>',afficher)
s1.bind('<Button-1>',afficher1) #Double-Button1 --> double clique 
s1.place(x=50,y=60)
bt1=Button(fen,text='Valider')
bt1.place(x=50,y=300)
#ouverture d'une autre fenêtre
bt2=Button(fen,text="ouverture d'une autre fenâtre",command=ouverture1)
bt2.place(x=50,y=150)

bt19=Button(fen,text="Exit",command=quitter)
bt19.place(x=500,y=300)
bt20=Button(fen,text="Effacer l'écran",command=effacer_ecran)
bt20.place(x=200,y=300)
fen.mainloop()



