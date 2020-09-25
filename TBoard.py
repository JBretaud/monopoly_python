import unittest

from classes.board import Board
from classes.player import Player
from classes.lot import Lot

class TBoard (unittest.TestCase):
    def Test__init__(self) :
        b = Board()
        unittest.assertTrue(len(b.Squares) == 40)


unittest.main()