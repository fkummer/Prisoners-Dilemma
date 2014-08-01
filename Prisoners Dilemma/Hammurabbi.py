__author__ = 'kummef'

import Prisoner

class Hammurabbi(Prisoner.Prisoner):

    def chooseNextMove(self):
        if(self.getPrevOppMove() == -1):
            return self.nice
        else:
            return self.getPrevOppMove()


