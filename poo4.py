class Eleve:
   
    moyenne=0.0 # attribut de classe

    def __init__(self,nom,prenom):
        self.nom=nom # attributs standard
        self.prenom=prenom
    def afficher(self,message): # méthode standard 
        print(f"élève {self.nom} {self.prenom} {message}" )
    
    # méthode de classe
  
    def calculer(self,d1,d2): # méthode de classe
       Eleve.moyenne=round((d1+d2*2)/3,2)
    calculer=classmethod(calculer)
    def définition():#méthode statique=>n'est pas lié a un objet ou une instance
        print(" vous ête un élève du lycéé taher sfar\n"
         "de sousse et vous ête en classe 4 math 2")
    définition=staticmethod(définition)

# avec (instance ou objet) en utiliser  classe standard =>méthode standard
e=Eleve("Boubaker","Ali")
e.afficher("Bonjour ")


print(e.calculer(12.3,14.20))

# sans instance on va utiliser objet de classe => méthode de classe
dc=float(input("Donner note de contrôle :"))
ds=float(input("Donner note de synthese :"))
Eleve.calculer(dc,ds)
print(Eleve.moyenne)
# ------------   =>méthode statique
Eleve.définition()


