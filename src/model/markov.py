import random
from model.trie import Trie

    
def rakenna_trie(opetusdata, aste=3):
    """ Trien rakennus """
    trie = Trie()
    for i in range(len(opetusdata)-aste + 1):
        jakso = opetusdata[i:i+aste]
        trie.insertti(jakso)
    return trie

def generoi_triella(trie, pituus, aloitus=None, aste=3):
    """ generoi triella """
    if aloitus is None:
        aloitus = random.choices(list(trie.juuri.lapset.keys()), k=aste)

    melodia = list(aloitus)
    for _ in range(pituus - len(aloitus)):
        konteksti = tuple(melodia[-aste:])
        seuraavat = trie.getter(konteksti)
        if not seuraavat:
            break
        seuraava = painotettu_valinta(seuraavat)
        melodia.append(seuraava)
    return melodia

def painotettu_valinta(vaihtoehdot):
    """ palauttaa yhden vaihtoehdon painotetulla arvonnalla """
    kaikki = []
    for jakso, maara in vaihtoehdot.items():
        kaikki.extend([jakso] * maara)
    return random.choice(kaikki)