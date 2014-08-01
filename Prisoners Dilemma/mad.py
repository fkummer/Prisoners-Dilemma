__author__ = 'kummef'

import Prisoner

class MAD(Prisoner.Prisoner):

    def chooseNextMove(self):
        #Be nice, but if you ever get treated badly never stop being mean
        if(self.isFirstTurn()):
            return self.getNice()
        elif(self.getPrevMove() == self.getNice()):
            if(self.getPrevOppMove() == self.getNice()):
                return self.getNice()
            else:
                return self.getMean()
        else:
            return self.getMean()