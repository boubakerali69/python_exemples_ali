dic={"un":"one","tow":"deux","tree":"troix"}
#pour acceder a un élément du dictionnaire
print(dic["un"])
# pour modifier un élèment dictionnaire
dic.update({"tow":"deux","tow":"2"})
print(dic)
# pour supprimer un élèment du dictionnaire
dic.pop("tow")
print(dic)