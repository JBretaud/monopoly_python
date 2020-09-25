class Joueur:
    def __init__(self,numero):
        self.numero = numero
    
    def ask_name(self):
        return input("Quel est le nom du joueur ", self.numero)

    