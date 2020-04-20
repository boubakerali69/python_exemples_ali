from math import *

liste=[10,20,8,-6,15,-8,30]
mess2="{:.2f} est negatif"
mess1="la racice carée est :{:.2f}"
for v in liste:
    try:
        print(mess1.format(sqrt(v)))
    except:
        print(mess2.format(v))
