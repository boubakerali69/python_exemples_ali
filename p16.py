from tkinter import *
from tkinter.messagebox import *
 # les fonctions
def affiche():
    lib1.config(text=int(s1.get())+"1")
    #lib1.set(s1.get())
def surv(*args):
    lib1_v.set(a.get()+10)
    


#


fen1=Tk()



fen1.geometry("600x500")

 #label
lib1_v=StringVar()
lib1=Label(fen1,textvariable=lib1_v,font=("arial",20),fg='blue',bg='yellow')
lib1.place(x=150,y=2)



# saisie de a
b=IntVar()

lib0=Entry(fen1,text="entree une valeur",textvariable=b)
lib0.place(x=100,y=200)


a=IntVar()
a.trace("w",surv)
a.set('entree la valeur de a')
s1=Entry(fen1,textvariable=a)
s1.place(x=100,y=100)

#s1.trace(context=1)

#bouton executer
b1=Button(fen1,text='Executer',command=surv)
b1.place(x=120,y=120)
fen1.mainloop()

