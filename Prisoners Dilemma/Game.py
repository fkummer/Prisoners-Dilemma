__author__ = 'kummef'

import Prisoner
import Human

class Game():

    def __init__(self, p1, p2, silent):
        self.p1 = p1
        self.p2 = p2
        self.p1Score = 0
        self.p2Score = 0
        self.silent = silent
        x = Prisoner.Prisoner()
        self.nice = x.getNice()
        self.mean = x.getMean()
        if(not self.silent):
            self.actionMessageOn = self.actionMessageToggle()
        else:
            self.actionMessageOn = False


    def playRound(self):
        p1Move = self.p1.chooseNextMove();
        self.p1.setPrevMove(p1Move)
        p2Move = self.p2.chooseNextMove();
        self.p2.setPrevMove(p2Move)
        self.printMessage(self.p1)
        self.printMessage(self.p2)

        self.p1.setPrevOppMove(p2Move)
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

    def playSet(self, rounds):
        self.p1Score = 0
        self.p2Score = 0
        self.p1.reset()
        self.p2.reset()

        i = 0
        while(i < rounds):
            self.playRound()
            i += 1

        if(not self.silent):
            print("Player 1:"+str(self.p1Score))
            print("Player 2:"+str(self.p2Score))

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
