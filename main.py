import sys
sys.path.append('C:/Users/hoc.F44M-HOCO-010/Documents/python/Monopoly')
from classes.lot import Lot
from classes.player import Player
from src import lots
lot = Lot(1)
print(lot.name)
print(lots[1]['name'])

player1 = Player (1, 1000,1,'chapeau')



player1.throw_dice()


