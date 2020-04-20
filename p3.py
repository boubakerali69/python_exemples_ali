class Homme:
    
   def __init__(self,nom,prenom):
       self.nom=nom
       self.prenon=prenom
      
   def afficher(self,age):
         print("nom: {}  prenom: {}".format(self.nom,self.prenon)+"age :"+str(age))

h1=Homme("ali","boubaker")
h1.afficher(15)


















