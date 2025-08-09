class TrieSolmu:
    """ Trien solmu """

    def __init__(self):
        self.lapset = {} 
        self.laskuri = 0


class Trie:
    """ Trie sekvensseille """

    def __init__(self):
        self.juuri = TrieSolmu()

    def insertti(self, sekvenssi):
        """ insertti
        
        """
        solmu = self.juuri
        for nuotti in sekvenssi:
            if nuotti not in solmu.lapset:
                solmu.lapset[nuotti] = TrieSolmu()
            solmu = solmu.lapset[nuotti]
            solmu.laskuri += 1

    def getter(self, konteksti):
        solmu = self.juuri
        for nuotti in konteksti:
            if nuotti in solmu.lapset:
                solmu = solmu.lapset[nuotti]
            else:
                return {}
        return {nuotti: lapsi.laskuri for nuotti, lapsi in solmu.lapset.items()}
