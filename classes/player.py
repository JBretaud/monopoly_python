from random import randrange

class Player:
    def __init__(self,numero,money):
        self.numero = numero
        self.money = 10
        
    def ask_name(self):
        return input("Quel est le nom du joueur ", self.numero)
    
    def throw_dice(self):
        lance1 = randrange(1,6)
        lance2 = randrange(1,6)

