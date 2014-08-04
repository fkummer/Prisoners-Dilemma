__author__ = 'kummef'

__author__ = 'kummef'


import Prisoner

class Human(Prisoner.Prisoner):

    def __init__(self):
        super().__init__()
        self.setName("Human")
        self.setNiceMessage(self.getName()+" was nice")
        self.setMeanMessage(self.getName()+" was mean")

    def chooseNextMove(self):
        moved = False
        if(self.isFirstTurn()):
            self.setName(input("Enter name:"))
        while(not moved):
            move = input("Enter your move(N for nice/M for mean):")
            if(move.lower() == "n"):
                return self.nice
                moved = True
            elif(move.lower() == "m"):
                return self.mean
                moved = True
            else:
                print("Please enter a valid move, either M for mean or N for nice")
