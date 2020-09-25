from .player import Player

class Bank:

    def __init__ (self, Players):
        self.Players = Players


    def Get_from_player(self, Player1, Money):
        Player1.money -= Money
        input ("ok")


    def Pay_to_player(self, Player1, Money):
         Player1.money += Money

    def Build_house(self):
        pass

    def Bidding(self, Lot):
        Bidders = Players
        while len(Bidders) > 1:
            for Bidder in Bidders:
                if not Bidder.Bid() : Bidders.remove(Bidder)
        Lot.Owner = Bidders[0]

    def Buy_Lot(self, Lot, Player):
        Lot.Owner = Player
    
    def Player_to_player_Transaction(self, Player1, Player2, Money):
        Player1.money -= Money
        Player2.money += Money
    
