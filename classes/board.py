import sys
sys.path.append('C:/Users/hoc.F44M-HOCO-010/Documents/python/Monopoly')
from src import squares
from classes.square import Square

class Board:
    def __init__(self):
        self.Create_Squares()

    def Create_Squares(self):
        self.squares = []
        i = 0
        while i < 40 :
            self.squares.append(Square(i))
            i+=1
            
    def To_Str(self):
        for square in self.squares:
            print(square.Name)


b = Board()
b.To_Str()