__author__ = 'kummef'

import Prisoner

class Hammurabbi(Prisoner.Prisoner):

    def __init__(self):
        super().__init__()
        self.setName("Hammurabbi")
        self.setNiceMessage("I would bring about the rule of law, so that the weak need not fear the strong.")
        self.setMeanMessage("Take an eye for an eye!")

    def chooseNextMove(self):
        #default is to play nice
        if(self.isFirstTurn()):
            return self.nice
        #it's an eye for an eye!
        else:
            return self.getPrevOppMove()


