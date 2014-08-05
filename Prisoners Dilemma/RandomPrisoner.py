__author__ = 'kummef'
import Prisoner
import random

class RandomPrisoner(Prisoner.Prisoner):

    def __init__(self):
        super().__init__()
        self.setName("Random")
        self.setNiceMessage("Wibbily woobly wobbly")
        self.setMeanMessage("Wazza mazza chazza")

    def chooseNextMove(self):
        x = random.randint(0,9)
        if(x >= 5):
            return self.mean
        else:
            return self.nice
