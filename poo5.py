def pluratize(total,singlar,plural=None):
    try:
        assert isinstance(total,int) and total>=0

    except:
        print('donner un entier positif')
    if not plural:
        plural=singlar+"s"
    ligne=singlar if total<=1 else plural
    return f'{total} {ligne}'

#programme principale
print(pluratize(5,"jour","joursssssssssss"))
