__author__ = 'kummef'
import Game
import Prisoner
import copy
import random

class EvolutionMode():

    def __init__(self, capacity):
        self.world = []
        self.capacity = capacity

    def addSpecies(self, type, number):
        i = 0
        while(i<number):
            self.world.append(copy.copy(type))
            i += 1

        random.shuffle(self.world)
        self.worldTrim()



    def worldTrim(self):
        #the world only has enough resources to support a certain number of prisoners, the capacity, so when we reach the limit, there's a 10% die off
        if(len(self.world) >= self.capacity):
            i = 0
            random.shuffle(self.world)
            while(i < (int)(.10*self.capacity) or len(self.world) > self.capacity):
                self.world.pop()
                i += 1


    def generation(self):
        newWorld = []
        while(len(self.world) > 1):
            firstIndex = random.randint(0, len(self.world)-1)
            first = self.world.pop(firstIndex)
            secondIndex = random.randint(0, len(self.world)-1)
            second = self.world.pop(secondIndex)
            conflict = Game.Game(first, second, True)
            conflict.playSet(5)
            newWorld = self.reproduce(conflict, newWorld)
        self.world = newWorld
        random.shuffle(self.world)
        self.worldTrim()





    def reproduce(self, game, world):
        babies1 = int(game.p1Score/3)
        babies2 = int(game.p2Score/3)
        i = 0
        j = 0
        while(i<babies1):
            world.append(copy.copy(game.p1))
            i += 1
        while(j<babies2):
            world.append(copy.copy(game.p2))
            j += 1

        return world

    def countSpecies(self):
        species = {}
        for prisoners in self.world:
            if(not prisoners.getName() in species):
                species[prisoners.getName()] = 1
            else:
                species[prisoners.getName()] += 1
        print(species)
