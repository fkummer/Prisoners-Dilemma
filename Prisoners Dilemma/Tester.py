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

x = EvolutionMode.EvolutionMode(2000)

x.addSpecies(Lucifer, 50)
x.addSpecies(Ham, 250)
x.addSpecies(JC, 50)
x.addSpecies(rando,1500)
#x.addSpecies(angry, 15)
x.countSpecies()
#x.addSpecies(poke, 40)


i = 0
while(i<100):
    x.generation()
    i += 1
print(len(x.world))




