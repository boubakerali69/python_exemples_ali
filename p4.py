class Voiture:
  
	def __init__(self):
		self.nom = "Ferrari"

	def donne_moi_le_modele(self):
		return "250"


v1=Voiture() 
print(v1.donne_moi_le_modele())

