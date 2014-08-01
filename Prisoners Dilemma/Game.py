__author__ = 'kummef'

import Prisoner

class Game():

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1Score = 0
        self.p2Score = 0
        x = Prisoner.Prisoner()
        self.nice = x.getNice()
        self.mean = x.getMean()

    def playRound(self):
        p1Move = self.p1.chooseNextMove();
        p2Move = self.p2.chooseNextMove();
        self.p1.setPrevMove(p1Move)
        self.p1.setPrevOppMove(p2Move)
        self.p2.setPrevMove(p2Move)
        self.p2.setPrevOppMove(p1Move)

        #both are nice
        if((p1Move == self.nice) and (p2Move == self.nice)):
            self.p1Score += 2
            self.p2Score += 2
            return

        #both are mean
        elif((p1Move == self.mean) and (p2Move == self.mean)):
            self.p1Score += 1
            self.p2Score += 1
            return

        #p1 throws p2 under the bus
        elif((p1Move == self.mean) and (p2Move == self.nice)):
            self.p1Score += 3
            self.p2Score += 0
            return

        #p2 throws p1 under the bus
        elif((p1Move == self.nice) and (p2Move == self.mean)):
            self.p1Score += 0
            self.p2Score += 3
            return
