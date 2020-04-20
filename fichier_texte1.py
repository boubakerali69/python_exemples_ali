fic2=open("art.txt","w") # w=>creation a nouveau et ajout/ a=> pour ajouter sur l'ancien contenu

with open("article.txt","r") as fic:
    data=fic.readline().split(";")
    print(data)
    """
    for ligne in fic:
        liste1=ligne.split(";")
        fic2.write(liste1[5]+"\n")
    """

fic2.close()

