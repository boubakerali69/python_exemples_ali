class eleves:

    def __init__(self, name,age):
        self.name = name
        self.age=age
       

    def parler(self, message):
       print(f"l'élève {self.name} a dit a tout le monde {message}")
       

e1=eleves("Balsam boubaker",17)
e1.parler("Bonjour")

