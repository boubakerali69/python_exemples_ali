
from tkinter import *
from tkinter.messagebox import *

def hello():
       showinfo( "Hello Python", "Hello World")


def  clickExitButton () :
         exit ()


fen1=Tk()
fen1.wm_title ( "Tkinter button" )
fen1.geometry ( "320x200" )
fen1.title("Mon premier Programme")

lib1=Label(fen1,text="Fiche client",font=30,fg="white",bg="blue").pack()

exitButton = Button ( text = "afficher" , command =hello) 
exitButton.place (x = 200,y = 10 )

exitButton = Button ( text = "Exit" , command =clickExitButton) 
exitButton.place (x = 200,y = 50 )



fen1.mainloop()

