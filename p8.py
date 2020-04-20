#classe mére
class Vehicule:
    def __init__(self,marque,couleur,puissance):
        self.marque=marque
        self.couleur=couleur
        self.puissance=puissance
    def kilom(self):
        print("La couleur de la voiture est :"+self.couleur)
# classe fille
class Voiture(Vehicule):
    def __init__(self,marque,couleur,puissance,annee,prix):
        Vehicule.__init__(self,marque,couleur,puissance)
        self.annee=annee
        self.prix=prix
    def affiche(self):
        print("marque="+self.marque)
        print("Couleur="+self.couleur)
        print("Puissance="+self.puissance)
        print("prix="+str(self.prix))
    def kilom(self):
        print("Puissance de la vourture (classe fille) ="+self.puissance)
        

    
    
v1=Voiture("BMW","Rouge","4CV",2011,15.000)
v1.affiche()
v1.kilom()







        
        