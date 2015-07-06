__author__ = 'kummef'

import Prisoner
import Human
import random

class Game():

    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p1Score = 0
        self.p2Score = 0
        self.p3Score = 0
        x = Prisoner.Prisoner()
        self.nice = x.getNice()
        self.mean = x.getMean()
        self.actionMessageOn = self.actionMessageToggle()

    def playRound(self):
        list = [self.p1, self.p2, self.p3]

        comp1 = self.p1
        comp2 = self.p2

        ind = random.randint(0,2)
        comp1 = list[ind]

        ind = random.randint(0,2)
        comp2 = list[ind]

        while (comp2 == comp1):
            ind = random.randint(0,2)
            comp2 = list[ind]

        comp1Move = comp1.chooseNextMove()
        comp1.setPrevMove(comp1Move)
        comp2Move = comp2.chooseNextMove()
        comp2.setPrevMove(comp2Move)

        #both are nice
        if((comp1Move == self.nice) and (comp2Move == self.nice)):
            comp1.score += 2
            comp2.score += 2


        #both are mean
        elif((comp1Move == self.mean) and (comp2Move == self.mean)):
            comp1.score += 1
            comp2.score += 1


        #p1 throws p2 under the bus
        elif((comp1Move == self.mean) and (comp2Move == self.nice)):
            comp1.score += 3
            comp2.score += 0


        #p2 throws p1 under the bus
        elif((comp1Move == self.nice) and (comp2Move == self.mean)):
            comp1.score += 0
            comp2.score += 3

        comp1.setPrevOppMove(comp2Move)
        comp2.setPrevOppMove(comp1Move)

        self.printMessage(comp1)
        self.printMessage(comp2)
        print("--------")

    def playSet(self, rounds):
        i = 0
        while(i < rounds):
            self.playRound()
            i += 1

        print("Player 1"+"("+self.p1.name+")"+":"+str(self.p1.score))
        print("Player 2"+"("+self.p2.name+")"+":"+str(self.p2.score))
        print("Player 3"+"("+self.p3.name+")"+":"+str(self.p3.score))
        self.p1.reset()
        self.p2.reset()
        self.p3.reset()

    def printMessage(self, player):
        if(self.actionMessageOn):
            if(player.getPrevMove() == player.getNice()):
                print(player.getNiceMessage()+"(Nice)")
            elif(player.getPrevMove() == player.getMean()):
                print(player.getMeanMessage()+"(Mean)")
            else:
                print("Invalid Move")

    def isHuman(self):
        if(isinstance(self.p1, Human.Human) or isinstance(self.p2, Human.Human)):
            return True

    def actionMessageToggle(self):
        if(not self.isHuman()):
            responded = False
            while(not responded):
                resp = input("Would you like to turn action messages on?(Y/N):")
                if(resp.lower() == "y"):
                    return True
                elif(resp.lower() == "n"):
                    return False
                else:
                    print("Please enter either Y for yes or N for no.")
        else:
            return True
