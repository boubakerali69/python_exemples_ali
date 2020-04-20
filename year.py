

def next_year():
    global year
    print("Fin de l'année en cours",year)
    year+=1
    print("Début de l'année suivante :",year)


year=int(input("donner l'année en cours :"))
next_year()

