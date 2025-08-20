import random
from typing import List, Tuple
from src.model.trie import Trie


KESTOT = [
    (0.25, "neljäsosa"), # neljäsosanuotti
    (0.5, "puolikas"), # puolinuotti
    (1.0, "koko") #  kokonainen nuotti
]

KESTOJEN_PAINOT = [0.6, 0.3, 0.1]
 

def sample_laskurista(lasketut):
    """ Arpoo seuraavan elementin Counterista"""
    summa = sum(lasketut.values())
    if summa <= 0:
        return None
    r = random.uniform(0, summa)
    acc = 0.0
    for k, v in lasketut.items():
        acc += v
        if r <= acc:
            return k
    return None

def sample_kesto() -> float:
    """ Palauttaa satunnaisen keston nuotille """
    return random.choices([d[0] for d in KESTOT], weights=KESTOJEN_PAINOT, k=1)[0]

def generoi_triella(trie: Trie, aloitus: List[str], pituus: int) -> List[Tuple[str, float]]:
    """ Generoi asteiden mukaan ja palauttaa listan tupleja"""
    n = trie.aste
    tulos: List[Tuple[str, float]] = []
    # varmistetaan että aloitus on tarpeeksi pitkä
    while len(tulos) < pituus:
        nuotit = list(aloitus[:n])
        fragmentti: List[Tuple[str, float]] = [(nuotti, sample_kesto()) for nuotti in nuotit]
        # alustetaan fragmentti ensimmäisillä nuoteilla
        while len(fragmentti) + len (tulos) < pituus:
            ikkuna = [nuotti for nuotti, _ in fragmentti[-n:]]
            etaisyys = trie.next_distribution(ikkuna)
            if not etaisyys:
                break
            seuraava = sample_laskurista(etaisyys)
            if seuraava is None:
                break
            fragmentti.append((seuraava, sample_kesto()))
        
        # varmistetaan että fragmentti on oikean pituinen
        tarvittava = pituus - len(tulos)
        tulos.extend(fragmentti[:tarvittava])

    return tulos