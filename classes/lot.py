import sys
sys.path.append('C:/Users/hoc.F44M-HOCO-010/Documents/python/Monopoly')

from src import lots
from src import stations
from src import companies
from src import squares


class Lot():
    def __init__(self,num):
        """
        Instancie un lot
        """
        cases = {**companies, **stations, **lots}
        self.name = cases[num]['name']
        self.mortgage = False
        self.house_price = cases[num]['house']
        self.color = squares[cases[num]['color']]
        self.owner = ""
        self.house_number = 0
        if num in companies :
            self.rent_company = [4,10]
            self.rent_stations = ""
            self.rent_lots = ""
        elif num in stations :
            self.rent_stations = [25,50,100,200]
            self.rent_lots = ""
            self.rent_company = ""
        elif num in lots :
            self.rent_lots = [lots[num]['loyer']]
            self.rent_stations = ""
            self.rent_company = ""
        else :
            raise Exception("numéro non reconnu")
        
    def get_rent(self, player):
        """
        Retourne la valeur du loyer à payer sur la case
        """
        if self.rent_stations != "" :
            return self.rent_stations[player.nb_stations_owned()-1]
        elif self.rent_company != "" :
            return self.rent_stations[player.nb_companies_owned()-1]*player.Dice_throw
        else :
            rent = self.rent_lots[self.house_number]
            if self.house_number == 0 and player.has_full_street:
                rent = rent*2
            return rent
    


