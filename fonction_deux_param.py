def parite(n):
    n1,n2=0,0
   
    for i in range(1,n+1):
        n1+=1 if i%2==0 else n2=n2+1
        return n1,n2

#programme principal
n=int(input("donner la valeur de n="))
nb_paire,nb_impaire=parite(n)
print(f"nombre des entiers paire :{nb_paire} nombre des entiers inpaire est {nb_impaire}")



