from classes.lot import Lot


class Streer(Lot):
    # Herite de la class Lot

     def __init__(self, nom_street, color, housse_price, rent_price):
         self.nom_street=nom_street
         self.color=color
         self.house_price=housse_price
         self.rent_price = rent_price
