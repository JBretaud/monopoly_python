from random import randrange
class De() :
    def __init__(self,nbFaces):
        if nbFaces > 0:
            self.nbFaces = int(nbFaces)
        else :
            raise Exception('Le nombre de faces doit être supérieur à 0')


    def launch(self):
        return randrange(1,self.nbFaces)
    
    

