from model.markov import MarkovGen
from model.trie import MelodiaTrie

class MelodiaGen:
    def __init__(self, malli_tyyppi="markov", aste=2):
        self.malli_tyyppi = malli_tyyppi.lower()
        self.aste = aste

        if self.malli_tyyppi == "markov":
            self.malli = MarkovGen(aste)
        elif self.malli_tyyppi == "trie":
            self.malli_tyyppi = MelodiaTrie()

    def opeta(self, sekvenssit):
        """ Tässä sekvenssi on lista tupleja """
        if self.malli_tyyppi == "markov":
            for i in sekvenssit:
                pass

    def generoi(self, pituus=50):
        """ generoi mallin """
        pass