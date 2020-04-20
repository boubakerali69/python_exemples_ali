#recursivite
def somme(a):
    a+=1
    print(a)
    if a<=10:
        somme(a)
somme(0)