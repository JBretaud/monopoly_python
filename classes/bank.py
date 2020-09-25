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
        Value = 0
        while len(Bidders) > 1:
            for Bidder in Bidders:
                bid = Bidder.Bid()
                if not bid :
                    Bidders.remove(Bidder)
                else :
                    Value = Bidder.Bid()
        self.Get_from_player(Bidders[0],Value)
        self.Buy_Lot(Bidders[0],Lot, Value)

    def Buy_Lot(self, Player, Lot, Value=-1):
        Lot.Owner = Player
        msg = Player.Name+" acquiere "+Lot.Name
        if Value != -1 : msg += " pour "+Value+" €."
        print(msg)
    
    def Player_to_player_Transaction(self, Player1, Player2, Money):
        Player1.money -= Money
        Player2.money += Money
    
