from tkinter import *
fen = Tk () # la fenêtre de l'application
# les labels
labelUn = Label (fen, text="votre prénom :")
labelUn.grid (row = 1,column = 1, sticky = "E", padx = 10)
labelDeux = Label (fen, text="votre nom :")
labelDeux.grid (row = 2, column = 1, sticky = "E", padx = 10)
labelTrois = Label (fen, text="votre ville :")
labelTrois.grid (row = 3, column = 1, sticky = "E", padx = 10)
labelValider = Label (fen, text="") # label de la chaîne de validation
labelValider.grid (row = 4, column = 1, columnspan = 2,\
sticky ="W",padx = 10)

fen.mainloop() # boucle de capture des événements
fen.destroy() # fin de l'application