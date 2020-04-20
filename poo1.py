class Humain():
    """
    Classe des êtres humain
    """
    #création d'un attribut ce classe
    compteur=0
    def __init__(self,nom,prenom,age):
        print("Création d'un humain")
        self.nom=nom
        self.prenom=prenom
        self.age=age
        Humain.compteur+=1
    def afficher1(self):
        return f"Nom est {self.nom}"
    def afficher2(self):
        return f"compteur={Humain.compteur:5.2f}"
    

print("lancement des tritament..............")
# instancier une classe et création de l'objet h.
h1=Humain("ali","boubaker",51.5)
#print(f"nom = {h1.nom} prenom = {h1.prenom} age={h1.age:10.2f}")
print(h1.afficher2())
h2=Humain("Balsem","boubaker",17.5)
print(h2.afficher2())

