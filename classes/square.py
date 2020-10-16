import sys
sys.path.append('C:/Users/hoc.F44M-HOCO-010/Documents/python/Monopoly')
from src import squares
from src import lots
from src import companies
from src import stations
from classes.lot import Lot

class Square:
    def __init__(self, num):
        self.Name = squares[num]
        self.Player = ""

        if num in [num for cle in {**lots,**companies,**stations}.keys()]:
            self.Lot = Lot(num)
        self.Event = 'Caisse de Communauté' if self.Name == 'Caisse de Communauté' else 'Carte Chance' if self.Name == 'Carte Chance' else ""
        self.Tax = 200 if self.Name == 'Impôts' else 100 if self.Name == 'Taxe de Luxe' else 0
        self.Prison = num == 30
    
    
