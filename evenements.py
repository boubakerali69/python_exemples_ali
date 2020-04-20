
from tkinter import *
from tkinter.messagebox import *
fenetre=Tk()

def clavier(event):
    touche = event.keysym
    print(touche) # affiche sur consol
    showinfo(touche) # affiche sur fenêtre

canvas = Canvas(fenetre, width=500, height=500)
canvas.focus_set()
canvas.bind("<Key>", clavier)
canvas.pack()
fenetre.mainloop()