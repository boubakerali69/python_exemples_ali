from tkinter import Tk, Button
from tkinter.messagebox import askretrycancel, showwarning,\
showinfo, showerror
maFenetre = Tk()
def comOK() :
    rep = showwarning ("message warning",\
    "ceci est un script d'illustration\n"+\
    "sur les \"message box\"")
def comInfo() :
    rep = showinfo ("message info",\
    "ceci est un script d'illustration\n"+\
    "sur les \"message box\"")
def comErreur() :
    rep = showerror ("message erreur",\
    "ceci est un script sur les \"message box\" \n"+\
    "et il ne prétend pas à autre chose ! ")
def comRetry() :
    rep = askretrycancel ("message Retry / Cancel",\
    "Attention ! vous allez quitter !!!\n"\
    + "cliquez \"Recommencer\" pour quitter\n"\
    + "et \"Annuler\" pour revenir à l'état antérieur")
    if rep :
        maFenetre.quit()
monBoutonOK = Button (maFenetre, text = "Avertissement", command=comOK)
monBoutonOK.pack(padx=80 , pady=20)
monBoutonInfo = Button (maFenetre, text = "Information", command=comInfo)
monBoutonInfo.pack(padx=80 , pady=20)
monBoutonErreur = Button (maFenetre, text = "Erreur", command=comErreur)
monBoutonErreur.pack(padx=80 , pady=20)
monBoutonRetry = Button (maFenetre, text = "Confirmer", command=comRetry)
monBoutonRetry.pack(padx=80 , pady=20)
monBoutonQuit = Button (maFenetre, text = "Quitter", command=maFenetre.quit)
monBoutonQuit.pack(padx=80 , pady=20)
maFenetre.mainloop()
maFenetre.destroy()