from tkinter import *
from tkinter.messagebox import askyesno
from a3_module_dialogue import Dialogue
class MonDialogue (Dialogue) :
    def habillage (self, cadreConteneur) :
        Label(cadreConteneur, text = "Nom").grid (row=0)
        Label(cadreConteneur, text = "Prénom").grid (row=1)
        self.saisieNom = Entry(cadreConteneur)
        self.saisiePrenom = Entry(cadreConteneur)
        self.saisieNom.grid(row=0, column = 1)
        self.saisiePrenom.grid (row=1, column = 1)
        return self.saisieNom
    def apply (self) :
        un = self.saisieNom.get()
        deux = self.saisiePrenom.get()
        self.resultat = un+" "+deux
        labelResultat.configure(text = self.resultat)
# programme principal
def popDialogue ():
    d= MonDialogue(racine, titre = "module d'essais",
    offx=-50, offy=-100)
def quitter () :
    if askyesno ("quitter l'application", "voulez-vous quitter ?") :
        racine.quit()


racine = Tk ()
racine.geometry("+300+200")
cadreRacine = Frame(racine)
cadreRacine.pack(padx=150, pady=100)
labelResultat = Label (cadreRacine, text="RESULTAT")
labelResultat.pack()
Button(cadreRacine, text = "Hello", \
command=popDialogue).pack(padx=10,pady=10)
Button(cadreRacine, text = "stop", \
command=quitter).pack(padx=10,pady=10)
# capture la demande de suppression
racine.protocol("WM_DELETE_WINDOW", quitter)
racine.mainloop()
racine.destroy()