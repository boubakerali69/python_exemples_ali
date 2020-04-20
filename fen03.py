from  tkinter import *

class Application(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.creer_widgets()

    def creer_widgets(self):
        self.label = Label(self, text="J'adore Python !")
        self.bouton = Button(self, text="Quitter", command=self.quit)
        self.label.pack()
        self.bouton.pack()



app = Application()
app.geometry("1000x600+100+50")
app.title("Ma Première App :-)")
app.mainloop()