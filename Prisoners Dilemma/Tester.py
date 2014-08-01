__author__ = 'kummef'

import Game
import JesusPrisoner
import SatanPrisoner
import Hammurabbi
import mad

JC = JesusPrisoner.JesusPrisoner()
Lucifer = SatanPrisoner.SatanPrisoner()
Ham = Hammurabbi.Hammurabbi()
angry = mad.MAD()



x = Game.Game(angry, Lucifer)

x.playSet(100)

x.playSet(500)

