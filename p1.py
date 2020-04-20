

 
print("----------------------- fonction lambda exemples 1 ------------------")
#avec un seul paramétre prixttc
ttc=lambda prixttc:prixttc+(prixttc*1.19)
# l'appel avec la variable ttc
print(ttc(200))

print("----------------------- fonction lambda exemples 2------------------")
# avec deux paramétres
calculer=lambda a,b:print("la somme de "+str(a)+" est "+str(b)+" est ",str(a+b))
calculer(10,20)





