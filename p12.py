from tkinter import *
from tkinter.messagebox import *

# fonctions

def afficher():
    lab1.config(text="lancement des mise a jour..............")

def afficher1():
    lab1.config(text="quitter")


def afficher2(nom):
    lab1.config(text=nom)


def afficher3():
    showinfo("Ali boubaker .............")

def recupere():
    showinfo("Alerte", s1.get())

def callback():
    if askyesno('Titre 1', 'Êtes-vous sûr de vouloir faire ça?'):
        showwarning('Titre 2', 'Tant pis...')
    else:
        showinfo('Titre 3', 'Vous avez peur!')
        showerror("Titre 4", "Aha")

#------------------------------------------------
couleur = 'blue'

#text1=StringVar()

fen1=Tk()
fen1.geometry("900x600")


#text1.set("Hello World !")
lab1=Label(fen1,text="Mon premier Programme",font=("Helvetica", 32))
lab1.config(fg=couleur)
lab1.pack()
lab1.config(text="Boubaker ali")

# bouton1
b1=Button(fen1,text="Valider",command=afficher)
b1.config(fg=couleur)
b1.pack(padx=1,pady=5,side=LEFT)

#bouton des saisies
mp=StringVar()
mp.set("Saisir le mot de passe")
s1=Entry(fen1,text=StringVar ,width=30)
s1.pack(padx=1,pady=10,side=LEFT)
#s1.pack_configure(padx=10,pady=10,side=LEFT)



# bouton Récupération
b2=Button(fen1,text="Récupération",command=recupere)
b2.config(fg=couleur)
b2.pack(padx=1,pady=15,side=LEFT)
#b2["fg"] = "red"

# bouton3
b3=Button(fen1,text="afficher",command=callback)
b3.config(fg=couleur)
b3.pack(padx=1,pady=20,side=LEFT)

# checkbutton
bouton = Checkbutton(fen1, text="Nouveau?")
bouton.pack(padx=1,pady=25,side=LEFT)

# radiobutton
value = StringVar()
bouton1 = Radiobutton(fen1, text="Oui", variable=value, value=1)
bouton2 = Radiobutton(fen1, text="Non", variable=value, value=2)
bouton3 = Radiobutton(fen1, text="Peu être", variable=value, value=3)
bouton1.pack()
bouton2.pack()
bouton3.pack()
# liste
liste = Listbox(fen1)
liste.insert(1, "Python")
liste.insert(2, "PHP")
liste.insert(3, "jQuery")
liste.insert(4, "CSS")
liste.insert(5, "Javascript")

liste.pack()

s = Spinbox(fen1, from_=0, to=10)
s.pack()

fen1.mainloop()

