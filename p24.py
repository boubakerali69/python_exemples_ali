from tkinter import *
from os import *

def effacer_ecran():
    system("cls")

def quitter():
    exit()
def traitement(event):
    print("il ya eu un événement")
    #print(event.keysym)
    #print(event.num)
    print(event)
    if event.num==1:
        print("le bouton gauche est pressé")
    elif event.num==3:
        print("Le bouton droite est pressé")
    else:
        print(event.keysym)
 
fen=Tk()
fen.title("Mon premier programme")
#fen.minsize(600,300)
#fen.maxsize(900,600)
fen.geometry("600x400+250+50")
lib1=Label(fen,text="Fiche client")
lib1.place(x=50,y=20)
fen.event_add('<<click>>','<Button-1>','<Button-2>','<Button-3>','<Key>')

fen.bind('<<click>>',traitement)

bt19=Button(fen,text="Exit",command=quitter)
bt19.place(x=500,y=300)
bt20=Button(fen,text="Effacer l'écran",command=effacer_ecran)
bt20.place(x=200,y=300)
fen.mainloop()



