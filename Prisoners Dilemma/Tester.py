__author__ = 'kummef'

import Game
import JesusPrisoner
import SatanPrisoner

JC = JesusPrisoner.JesusPrisoner()
Lucifer = SatanPrisoner.SatanPrisoner()


x = Game.Game(JC, Lucifer)
x.playRound()
print(x.p1Score)
print(x.p2Score)