import sys
sys.path.append('C:/Users/hoc.F44M-HOCO-010/Documents/python/Monopoly')

from random import randrange
from src import lots

class Player:
    def __init__(self,numero,money):
        self.numero = numero
        self.money = 10
        self.dice_throw = 0
        self.turns_left_in_jail = 0
        self.nb_double_this_turn = 0
        self.nb_stations_owned = 0
        self.nb_companies_owned = 0
        self.owned_streets = []
        
    def ask_name(self):
        return input("Quel est le nom du joueur ", self.numero)
    
    def throw_dice(self):
        """
        Simule le lancement de deux D6,
        Inscrit le résultat dans les attributs du joueur
        S'il s'agit d'un double, incrémente le nombre de doubles lancés pendant le même tour
        """
        lance1 = randrange(1,6)
        lance2 = randrange(1,6)
        if lance1 == lance2 :
            self.nb_double_this_turn += 1
        self.dice_throw = randrange(1,6) + randrange(1,6)
    
    
    def has_full_street(self,num_street):
        """
        Teste si le joueur possède toutes les rues du numéro de case passé en paramètre
        """
        i = 0
        for key in lots.keys() :
            if lots[key].color == lots[num_street].color :
                i+=1
        for key in self.owned_streets:
            if lots[key].color == lots[num_street].color :
                i-=1
        return i == 0
