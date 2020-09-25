from classes.player import Player
from classes.bank import Bank

from unittest import main
from unittest import TestCase




class TBank (TestCase):
    def TGet_from_player(self):
        Bank = Bank()
        Player1 = Player()
        Player1.money = 1000

        Bank.Get_from_player(Player1, 100)
        self.assertTrue(Player1.money==900)


    def TPay_to_player(self):
        Bank = Bank()
        Player1 = Player()
        Player1.money = 1000

        Bank.Pay_to_player(Player1, 100)
        self.assertTrue(Player1.money==1100)

    def TBuild_house(self):
        pass

    def TBidding(self):
        pass

    def TBuy_Lot(self):
        pass

    def TPlayer_to_player_Transaction(self):
        pass

main()