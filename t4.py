
from tkinter import *
from tkinter.messagebox import *
fen1=Tk()
Button(fen1, text ="man", relief=RAISED, cursor="man").pack()

Canvas(fen1, width=400, height=150, bg='ivory').pack(side=LEFT, padx=5, pady=5)
Button(fen1, text ='Bouton 1').pack(side=TOP, padx=5, pady=5)
Button(fen1, text ='Bouton 2').pack(side=BOTTOM, padx=5, pady=5)

fen1.mainloop()

