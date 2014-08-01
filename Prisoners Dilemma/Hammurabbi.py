__author__ = 'kummef'

import Prisoner

class Hammurabbi(Prisoner.Prisoner):

    def chooseNextMove(self):
        if(self.isFirstTurn()):
            return self.nice
        else:
            return self.getPrevOppMove()


