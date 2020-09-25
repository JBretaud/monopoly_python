import sys
sys.path.append('C:/Users/hoc.F44M-HOCO-010/Documents/python/Monopoly')
from classes.lot import Lot
from src import lots
lot = Lot(1)
print(lot.name)
print(lots[1]['name'])