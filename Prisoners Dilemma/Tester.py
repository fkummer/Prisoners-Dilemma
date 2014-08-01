__author__ = 'kummef'

import Game
import JesusPrisoner
import SatanPrisoner

JC = JesusPrisoner.JesusPrisoner()
Lucifer = SatanPrisoner.SatanPrisoner()


x = Game.Game(JC, Lucifer)

x.playSet(100)

x.playSet(500)