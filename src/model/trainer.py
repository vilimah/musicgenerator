from typing import List
from collections import Counter
from src.model.trie import Trie
from src.model.markov import generoi_triella, sample_laskurista

class Trainer:
    """ Trie mallin opetus ja nuottisekvenssin generointi """
    def __init__(self, aste=10):
        self.aste = aste
        self.sekvenssit = []
        self.aloitukset: List[tuple] = []
        self.aloitukset_laskuri: Counter = Counter()

    def lisaa_sekvenssi(self, sekvenssi: List[str]):
        """ lisää nuottisekvenssiin aloitusikkunan """
        if len(sekvenssi) >= self.aste:
            aloitus_ikkuna = tuple(sekvenssi[:self.aste])
            self.aloitukset.append(aloitus_ikkuna)
            self.aloitukset_laskuri[aloitus_ikkuna] += 1

    def fit(self, sekvenssit: List[List[str]]) -> Trie:
        """ rakentaa trie-rakenteen annetusta listasta"""
        trie = Trie(self.aste)
        for sek in sekvenssit:
            trie.insertti(sek)
        return trie
    
    def rakenna_trie(self):
        """ rakentaa trie-rakenteen """
        return self.fit(self.sekvenssit)
    
    def painotettu_aloitus(self) -> List[str]:
        """ palauttaa satunnaisen aloitusikkunan painotetulla valinnalla"""
        if not self.aloitukset_laskuri:
            return []
        valinta = sample_laskurista(self.aloitukset_laskuri)
        return list(valinta)
    
    def generoi(self, trie: Trie, pituus: int, aloitus: List[str]) -> List[str]:
        """ generoi sekvenssin triellä"""
        if not aloitus or len(aloitus) < self.aste:
            aloitus = self.painotettu_aloitus()
        return generoi_triella(trie, aloitus, pituus)
    
    def lataa_opetusdata(self, sekvenssit: List[List[str]]):
        """ lataa opetusdatan """
        self.sekvenssit = sekvenssit
        for sek in sekvenssit:
            self.lisaa_sekvenssi(sek)
