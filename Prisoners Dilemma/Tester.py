__author__ = 'kummef'

import Game
import JesusPrisoner
import SatanPrisoner
import Hammurabbi
import mad

JC = JesusPrisoner.JesusPrisoner()
Lucifer = SatanPrisoner.SatanPrisoner()
Ham = Hammurabbi.Hammurabbi()
Sam = Hammurabbi.Hammurabbi()
Mad = mad.MAD()


x = Game.Game(Mad, Ham)

x.playSet(100)

x.playSet(500)

