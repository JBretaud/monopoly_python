from classes.lot import Lot


class Station(Lot):
    # Herite de la class Lot

     def __init__(self, nom_station, price):
         self.nom_station=nom_station
         self.price=price
