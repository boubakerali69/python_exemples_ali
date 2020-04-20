
# syntaxe % ==>  syntaxe vieille
name="Boubaker"
age=20
note=10.25
print("Mon prénom est : %s et j'ai l'age de %d ans avec une note=%f"%(name,age,note))

# syntaxe avec format() ==> avec python version 3.1
a=10.23652
b=20.36
print("la valeur de a est {1:10.2f} et la valeur de b est {0}".format(a,b))

# syntaxe avec "f-string" ==> nouveau syntaxe
a=125120.3362
b=53.362
print(f"la valeur de a est:{a:10.2f} et la valeur de b est {b}")