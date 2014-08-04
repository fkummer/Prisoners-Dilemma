__author__ = 'kummef'

import Prisoner



class SatanPrisoner(Prisoner.Prisoner):

    def __init__(self):
        super().__init__()
        self.setName("Satan")
        self.setNiceMessage("Nice? What the heck is that?")
        self.setMeanMessage("I'm the devil, what did you expect me to do!")

    def chooseNextMove(self):
        return self.mean
