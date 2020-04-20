from tkinter import Tk, Button
from tkinter.messagebox import askokcancel, askyesno, askquestion
maFenetre = Tk()
def comOK() :
    rep = askokcancel ("message OK/cancel",\
    "vous voulez terminer ???")
    if rep :
        maFenetre.quit()
def comOui() :
    rep = askyesno ("message oui/non",\
    "voulez-vous continuer ?")
    if not rep :
        maFenetre.quit()
def comQuestion() :
    rep = askquestion ("message question",\
    "voulez-vous continuer ?")
    if rep=="no" :
        maFenetre.quit()
monBoutonOK = Button (maFenetre, text = "OK / Annuler", command=comOK)
monBoutonOK.pack(padx=80 , pady=20)
monBoutonOui = Button (maFenetre, text = "oui / non", command=comOui)
monBoutonOui.pack(padx=80 , pady=20)
monBoutonQuestion = Button (maFenetre, text = "question",\
command=comQuestion)
monBoutonQuestion.pack(padx=80 , pady=20)
maFenetre.mainloop()
maFenetre.destroy()