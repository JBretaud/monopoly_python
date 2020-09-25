import sys
sys.path.append('C:/Users/hoc.F44M-HOCO-010/Documents/python/Monopoly')
from classes.square import Square
from classes.lot import Lot
import unittest
class TSquare (unittest.TestCase):
    def Test_Create_Lot(self):
        lot = Square(1)
        unittest.assertTrue(type(lot.Lot) == Lot)
        
    def Test_Create_Chance(self):
        chance = Square(7)
        unittest.assertTrue( chance.Event == 'Carte Chance' )

    def Test_Create_Commu(self):
        commu = Square(2)
        unittest.assertTrue( commu.Event == 'Caisse de Communauté' )

    def Test_Create_tax(self):
        tax = Square(4)
        unittest.assertTrue(tax.Tax == 200)

    def Test_Create_Prison(self):
        prison = Square(30)
        unittest.assertTrue(prison.Prison == True)

unittest.main()
