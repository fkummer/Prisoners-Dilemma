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
import EvolutionMode

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

x = EvolutionMode.EvolutionMode(1000)

x.addSpecies(Lucifer, 3)
x.addSpecies(Ham, 3)
x.addSpecies(JC, 3)
x.addSpecies(rando,3)
x.addSpecies(angry, 3)
x.addSpecies(poke, 3)


i = 0
while(i<200):
    x.generation()
    i += 1
print(len(x.world))
x.countSpecies()



