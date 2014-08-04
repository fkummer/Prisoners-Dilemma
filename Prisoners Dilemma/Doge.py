__author__ = 'smh'

import Prisoner

class Doge(Prisoner.Prisoner):

    def chooseNextMove(self):
        #repeats what opponent last did
        return self.getPrevOppMove()
