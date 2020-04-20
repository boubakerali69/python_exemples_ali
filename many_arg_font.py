# création d'une  fonction avec plusieurs paramètres
def afficher(*names):
    for n in names:
        print(n)

def somme(*var):
    s=0
    for v in var:
        s=s+v
    
    return s


print(somme(10.5,20,30.3))    
#afficher("ali","balsem","najoua")
