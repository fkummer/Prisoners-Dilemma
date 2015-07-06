__author__ = 'kummef'

class Prisoner:

    #when prevMove=-1 or prevOppMove=-1 then they have yet to make their first move
    #when both =-1 then it is the First Turn (see isFirstTurn())
    def __init__(self):
        self.nice = 0
        self.mean = 1
        self.prevMove = -1
        self.prevOppMove = -1
        self.niceMessage = "I was nice"
        self.meanMessage = "I was mean"
        self.name = "Prisoner"
        self.score = 0;

    def getNice(self):
        return self.nice

    def getMean(self):
        return  self.mean

    #default is to always be nice
    def chooseNextMove(self):
        return self.nice

    def setPrevMove(self, prevMove):
        self.prevMove = prevMove

    def setPrevOppMove(self, prevOppMove):
        self.prevOppMove = prevOppMove

    def getPrevMove(self):
        return self.prevMove

    def getPrevOppMove(self):
        return self.prevOppMove

    def isFirstTurn(self):
        if((self.prevMove == -1) and (self.prevOppMove == -1)):
            return True
        else:
            return False

    def reset(self):
        self.prevMove = -1
        self.prevOppMove = -1

    def getNiceMessage(self):
        return self.niceMessage

    def getMeanMessage(self):
        return self.meanMessage

    def setNiceMessage(self, message):
        self.niceMessage = message

    def setMeanMessage(self, message):
        self.meanMessage = message

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName