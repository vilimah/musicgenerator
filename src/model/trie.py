class TrieSolmu:
    """ Trie tietorakenne
    """
    def __init__(self):
        self.lapset = {}
        self.paate = False # onko päätepiste vai ei
        self.arvo = None # lisäarvo

class MelodiaSolmu:
    def __init__(self):
        self.juuri = TrieSolmu() # juurisolmu

    def insertti(self, avain, arvo=None):
        solmu = self.juuri
        for symboli in avain: # käy läpi syötteen
            if symboli not in solmu.lapset: # tässä luodaan uusi solmu jos symbolia ei ole
                solmu.lapset[symboli] = TrieSolmu()
            solmu = solmu.lapset[symboli]
        solmu.arvo = arvo
        solmu.paate = True
