#%%
from collections import namedtuple
from math import ceil

Lanka = namedtuple("Lanka", "nimi paino pituus")

l1 = Lanka("Cashmere Dreams", 25, 290)
l2 = Lanka("Kid Mohair", 50, 400)

Ohje = namedtuple("Ohje", "lanka menekki")
laberinto = Ohje(l2, 140)

uusi_menekki = laberinto.menekki*(laberinto.lanka.pituus/laberinto.lanka.paino)*(l1.paino/l1.pituus)
kerien_määrä = ceil(uusi_menekki/l1.paino)


