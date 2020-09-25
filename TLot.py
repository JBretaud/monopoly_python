import unittest
import sys
sys.path.append('C:/Users/hoc.F44M-HOCO-010/Documents/python/Monopoly')
from classes.lot import Lot
from src import lots

class Test_Lot(unittest.TestCase) :
    def test_lot(self):
        lot = Lot(1)
        unittest.assertEquals(lot.name, lots[1]['name'])

unittest.main()