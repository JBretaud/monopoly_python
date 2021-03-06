
import unittest

from classes.bank import Bank
from classes.player import Player
from classes.lot import Lot


class TBank (unittest.TestCase):
    
    def TGet_from_player(self):
        Player1 = Player()
        Player1.money = 1000
        Bank.Get_from_player(Player1, 100)
        unittest.assertTrue(Player1.money==900)


    def TPay_to_player(self):
        Player1 = Player()
        Player1.money = 1000
        Bank.Pay_to_player(Player1, 100)
        unittest.assertTrue(Player1.money==1100)

    def TBuild_house(self):
        pass

    def TBidding(self):
        C = Card()
        Bank.bidding(C)
        

    def TBuy_Lot(self):
        L = Lot()
        P = Player()
        Bank.Buy_Lot(L,P)
        unittest.assertTrue(L.Owner == P)

    def TPlayer_to_player_Transaction(self):
        P1 = Player()
        P2 = Player()
        initMoneyP1 = P1.money
        initMoneyP2 = P2.money
        Bank.Player_to_player_Transaction(P1,P2,100)
        unittest.assertTrue(P1.money == initMoneyP1 - 100 and P2.money == initMoneyP2 + 100)

unittest.main()