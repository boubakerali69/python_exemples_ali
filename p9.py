
class Voiture:
    def __init__(self,_roues):
        self._roues=4

    def _get_roues(self):
        print ("Récupération du nombre de roues")
        return self._roues

    def _set_roues(self, v):
        print ("Changement du nombre de roues")
        self._roues  =  v

    roues=property(_get_roues(), _set_roues(10))
    
v1=Voiture(4)

print(v1.roues)
