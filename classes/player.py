from random import randrange

class Player:
    def __init__(self,numero):
        self.numero = numero
        
    def ask_name(self):
        return input("Quel est le nom du joueur ", self.numero)
    
    def launch_dice(self):
        lance1 = randrange(1,6)
        lance2 = randrange(1,6)

