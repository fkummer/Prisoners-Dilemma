__author__ = 'kummef'

import Prisoner

class Hammurabbi(Prisoner.Prisoner):

    def chooseNextMove(self):
        #default is to play nice
        if(self.isFirstTurn()):
            return self.nice
        #it's an eye for an eye!
        else:
            return self.getPrevOppMove()


