"""
En général, les variables d'instance stockent des informations relatives à chaque instance 
alors que les variables de classe servent
 à stocker les attributs et méthodes communes à toutes les instances de la classe :
 exemples:
tricks = []             # mistaken use of a class variable
compteur=0

"""
class Dog:
  
     # mistaken use of a class variable
    compteur=0
    def __init__(self, name):
        self.name = name
        self. tricks = [] 
   
    def add_trick(self, trick):
        self.tricks.append(trick)
        Dog.compteur+=1


d1=Dog("Caniche")
d2=Dog("Berger Allemend")
d1.add_trick("Tunisie")
d2.add_trick("Algerie")
print(d1.tricks)
print(d2.tricks)
print(d1.compteur)


