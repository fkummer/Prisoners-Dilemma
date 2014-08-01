__author__ = 'kummef'
#As in Mutually Assured Destruction
import Prisoner

class MAD(Prisoner.Prisoner):

    def chooseNextMove(self):
        #Be nice, but if you ever get treated badly never stop being mean
        if(self.getPrevMove() == self.getNice()):
            if((self.isFirstTurn()) or (self.getPrevOppMove() == self.getNice())):
                return self.getNice()
            else:
                return self.getMean()
        else:
            return self.getMean()