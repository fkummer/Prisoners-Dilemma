__author__ = 'smh'

import Prisoner

class Doge(Prisoner.Prisoner):

    def __init__(self):
        super().__init__()
        self.setName("Doge")
        self.setNiceMessage("Wow, such nice")
        self.setMeanMessage("Very mean")

    def chooseNextMove(self):
        #repeats what opponent last did
        return self.getPrevOppMove()
