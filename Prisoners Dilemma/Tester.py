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

x.addSpecies(Ham, 3)
x.addSpecies(JC, 3)
x.addSpecies(Lucifer, 3)

print(x.world)
print(len(x.world))
x.generation()
print(len(x.world))
print(x.world)
x.generation()
x.generation()
x.generation()
x.generation()
x.generation()
print(len(x.world))
print(x.world)



