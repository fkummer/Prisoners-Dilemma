__author__ = 'kummef'

import Game
import JesusPrisoner
import SatanPrisoner
import Hammurabbi
import mad
import PokeyPrisoner
import Doge
import Human
import RandomPrisoner

JC = JesusPrisoner.JesusPrisoner()
Lucifer = SatanPrisoner.SatanPrisoner()
Ham = Hammurabbi.Hammurabbi()
angry = mad.MAD()
poke = PokeyPrisoner.PokeyPrisoner()
bloke = PokeyPrisoner.PokeyPrisoner()
d1 = Doge.Doge()
d2 = Doge.Doge()
hugh = Human.Human()
rando = RandomPrisoner.RandomPrisoner()

x = Game.Game(Lucifer, Ham, JC )

x.playSet(10000)


