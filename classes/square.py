import sys
sys.path.append('C:/Users/hoc.F44M-HOCO-010/Documents/python/Monopoly')
from src import cases
from src import proprietes
from classes.lot import Lot

class Square:
    def __init__(self, num):
        self.Name = cases[num]
        self.Player = ""
        if num in [num for cle in proprietes.keys()]:
            self.Lot = Lot(num)
        self.Event = 'Caisse de Communauté' if Name == 'Caisse de Communauté' else 'Carte Chance' if Name == 'Carte Chance' else ""
        self.Tax = 200 if Name == 'Impôts' else 100 if Name == 'Taxe de Luxe' else 0
        self.Prison = num == 30
    
    
