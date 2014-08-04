__author__ = 'kummef'

import Prisoner

class JesusPrisoner(Prisoner.Prisoner):
    def __init__(self):
        super().__init__()
        self.setName("Jesus")
        self.setMeanMessage("Something has gone very wrong here")
        self.setNiceMessage("Do unto others as you would have them do unto you!")

    def chooseNextMove(self):
        return self.nice

