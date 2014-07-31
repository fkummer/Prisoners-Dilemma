__author__ = 'kummef'

class Prisoner:

    def __init__(self, prevMove):
        self.nice = 0
        self.mean = 1
        self.prevMove = prevMove

    #default is to always be nice
    def chooseNextMove(self):
        return self.nice
