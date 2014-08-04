__author__ = 'kummef'
import Prisoner

class PokeyPrisoner(Prisoner.Prisoner):
    pokes = 0
    def chooseNextMove(self):
        if(self.pokes < 3):
            self.pokes += 1
            return self.getNice()
        else:
            #Test this guy out, see if he's a total push over
            if(self.getPrevOppMove() == self.getNice()):
                return self.mean
            #If he fights back backpedal and act nice again!
            else:
                self.pokes = 0
                return self.nice
