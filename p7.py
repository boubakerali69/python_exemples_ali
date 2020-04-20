#début définition
class Personne:
#Classe Personne"""
#constructeur
    def __init__(self):
        #lister les champs
        self.nom = ""
        self.age = 0
        self.salaire = 0.0
#fin constructeur
#saisie des infos
    def saisie(self):
        self.nom = input("Nom : ")
        self.age = int(input("Age : "))
        self.salaire = float(input("Salaire : "))
#fin saisie
#affichage des infos
    def affichage(self):
        print("Son nom est ", self.nom)
        print("Son âge : ", self.age)
        print("Son salaire : ", self.salaire)
#fin affichage
#fin définition

p1=Personne()
p1.saisie()
p1.affichage()

