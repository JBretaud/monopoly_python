from unittest import main
from unittest import TestCase
from unittest import assertTrue
from classes.bank import Bank
from classes.player import Player
from classes.lot import Lot

class TBank (TestCase):
    def TGet_from_player(self):
        pass

    def TPay_to_player(self):
        pass

    def TBuild_house(self):
        pass

    def TBidding(self):
        # C = Card()
        # Bank = Bank()
        # Bank.bidding(C)
        pass

    def TBuy_Lot(self):
        L = Lot()
        P = Player()
        Bank = Bank()
        Bank.Buy_Lot(L,P)
        assertTrue(L.Owner == P)

    def TPlayer_to_player_Transaction(self):
        P1 = Player()
        P2 = Player()
        initMoneyP1 = P1.money
        initMoneyP2 = P2.money
        Bank = Bank()
        Bank.Player_to_player_Transaction(P1,P2,100)
        assertTrue(P1.money == initMoneyP1 - 100 and P2.money == initMoneyP2 + 100)

main()