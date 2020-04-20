months = {
    "january": 31,
    "february": 28,
    "march": 31,
    "april": 30,
    "may": 31,
    "june": 30,
    "july": 31,
    "august": 31,
    "september": 30,
    "october": 31,
    "november": 30,
    "december": 31
}

# Un second dictionnaire d'association des noms de mois français / anglais
frTranslator = {
    "janvier": "january",
    "février": "february",
    "mars": "march",
    "avril": "april",
    "mai": "may",
    "juin": "june",
    "juillet": "july",
    "août": "august",
    "septembre": "september",
    "octobre": "october",
    "novembre": "november",
    "décembre": "december"
}

#programme principal
mois=input("Donner le nom du mois :")
if mois == "exit":
    print("quitter")
elif mois in months:
    print("le mois est {} et le nombre des jours est égale à {}".format(mois,months[mois]))
elif mois in frTranslator:
    print("le mois est {} et le nombre des jours est égale à {}".format(frTranslator[mois],months[frTranslator[mois]]))

else:
    print("erreur de saisie..............")


