
def afficher(nom,prenom):
    print("Bonjour mr {}".format(nom))
    print(f"Salut MR {prenom}")
def convertir(f):
    res= (f-32)*5/9
    return round(res,3)


n=input("Donner votre nom :")
m=input("Donner votre prénom :")
t=int(input("Donner la temperature en gédré fahrenheit :"))
afficher(n,m)
print(f"le résultat en dégre celsius  :{convertir(t)} °C")

