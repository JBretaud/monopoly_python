from .player import Player

class Bank:


    @staticmethod
    def Get_from_player(self, Player1, Money):
        Player1.money -= Money
        input ("ok")

    @staticmethod
    def Pay_to_player(self, Player1, Money):
         Player1.money += Money

    @staticmethod
    def Build_house(self):
        pass

    @staticmethod
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

    @staticmethod
    def Buy_Lot(self, Player, Lot, Value=-1):
        Lot.Owner = Player
        msg = Player.Name+" acquiere "+Lot.Name
        if Value != -1 : msg += " pour "+Value+" €."
        print(msg)
        
    @staticmethod
    def Player_to_player_Transaction(self, Player1, Player2, Money):
        Player1.money -= Money
        Player2.money += Money
    
