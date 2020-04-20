# -*-coding:Utf-8 -*

from tkinter import *


# - - - - - - - - - - - - - - - - - -

# Déclarations des fonctions utilisées

# - - - - - - - - - - - - - - - - - -


def mise_a_jour():

    monTexte.set("Et voilà !")


# - - - - - - - - - - - - - - - - - -

# Création de la fenêtre et des objets associés la fenêtre

# - - - - - - - - - - - - - - - - - -


fen_princ = Tk()


# Création d'un Label nommé monAffichage ayant monTexte comme textvariable

monTexte = StringVar()

monTexte.set("Texte de base !")

monAffichage = Label(fen_princ, textvariable = monTexte)

monAffichage.pack()


# Création d'un Button lancant la fonction mise_a_jour

monBouton = Button(fen_princ, text = "Mise à jour du texte ci-dessus", command=mise_a_jour)

monBouton.pack()


# - - - - - - - - - - - - - - - - - -

# Bouclage de la fenêtre fen_princ

# - - - - - - - - - - - - - - - - - -


fen_princ.mainloop()