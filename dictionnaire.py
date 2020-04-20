from os import *
system("cls")
user={
    "nom":"ali",
    'prenom':"Boubaker",
    "age":25
}
# acceder  a un élèment du dictionnaire
print ('---------- début de accés a un élément --------------------')
print(user['prenom'])


#loop en utilisant la méthode keys()
print ('---------- début de loop 1 --------------------')
for k in user.keys():
    print (k)
#loop en utilisant la méthode values()
print ('---------- début de loop 2 --------------------')
for v in user.values():
    print(v)
#loop pour afficher les deux keys et values
for k,v in user.items():
    print(k,"-->",v)
#comment ajouter un article(article=item en anglais) au dictionnaire
user["motde passe"]="200369"
for k,v in user.items():
    print(k,"-->",v)
    


