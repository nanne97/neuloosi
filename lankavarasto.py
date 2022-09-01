#%%
from lanka import Lanka
import json


dreams = Lanka("Cashmere Dreams", 25, 290)
mohair = Lanka("Mohair", 25, 212)


def laske_menekki(menekki, ohjeen_lanka, oma_lanka):
    return menekki * ohjeen_lanka.grams_in_m * oma_lanka.meters_in_g

#%%

uusi_menekki = laske_menekki(225, mohair, dreams)
kerät = uusi_menekki/dreams.paino
