from collections import Counter
from typing import Tuple, List, Optional

class TrieSolmu:
    """ Trien solmu """

    def __init__(self):
        self.lapset = {}
        self.laskuri: Counter = Counter()

class Trie:
    """ Trie sekvensseille """

    def __init__(self, aste: int):
        assert aste >= 1
        self.aste = aste
        self.juuri = TrieSolmu()

    def insertti(self, sekvenssi: List[str]):
        """ insertti: luo ikkunoita """
        n = self.aste
        if len(sekvenssi) < n+1:
            return
        for i in range(len(sekvenssi) - n):
            ikkuna = sekvenssi[i:i+n]
            seuraava = sekvenssi[i+n]
            solmu = self._node_for(ikkuna, luo=True)
            solmu.laskuri[seuraava] += 1


    def _node_for(self, ikkuna: List[str], luo: bool = False) -> Optional[TrieSolmu]:
        """ palauttaa solmun annetulle ikkunalle, luo tarvittaessa """
        solmu = self.juuri
        for symboli in ikkuna:
            if symboli not in solmu.lapset:
                if not luo:
                    return None
                solmu.lapset[symboli] = TrieSolmu()
            solmu = solmu.lapset[symboli]
        return solmu
    
    def next_distribution(self, ikkuna: List[str]) -> Counter:
        """ palauttaa Counterin jossa nuotit ja niiden lukumäärät"""
        solmu = self._node_for(ikkuna, luo=False)
        if solmu is None:
            return Counter()
        return solmu.laskuri.copy()
    
    def kaikki_ikkunat(self) -> List[Tuple[str, ...]]:
        """ palauttaa listan kaikista trieen tallennetuista ikkunoista"""
        res = []
        stack = [([], self.juuri)]
        while stack:
            path, solmu = stack.pop()
            if len(path) == self.aste:
                res.append(tuple(path))
            if len(path) < self.aste:
                for sym, lapsi in solmu.lapset.items():
                    stack.append((path + [sym], lapsi))
        return res