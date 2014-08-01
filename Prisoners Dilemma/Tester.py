__author__ = 'kummef'

import Game
import JesusPrisoner
import SatanPrisoner
import Hammurabbi

JC = JesusPrisoner.JesusPrisoner()
Lucifer = SatanPrisoner.SatanPrisoner()
Ham = Hammurabbi.Hammurabbi()


x = Game.Game(Lucifer, Ham)
x.playRound()
x.playRound()
x.playRound()
print(x.p1Score)
print(x.p2Score)