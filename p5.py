#appel du module
import modulespersonne as MP
#instanciation
p = MP.Personne()
#affiche tous les membres de p
print(dir(p))
#affectation aux champs
p.nom = input("Nom : ")
p.age = int(input("Age : "))
p.salaire = float(input("Salaire : "))
#affichage
print(p.nom,", ",p.age,", ",p.salaire)
