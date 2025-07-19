import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# aja tämä koodi ja jos tulee lukemaan "testit ok" niin testin tulisi toimia oikein


from src.model.trie import MelodiaTrie

def testaa_melodia_trie():
    """ testi funktio trielle
    """
    trie = MelodiaTrie()

    melodia1 = (60, 62, 64) # C, D, E
    melodia2 = (60, 62, 65) # C, D, F
    melodia3 = (64, 65, 67) # E, F, G

    trie.insertti(melodia1, "melodia 1")
    trie.insertti(melodia2, "melodia 2")
    trie.insertti(melodia3, "melodia 3")

    def haku(trie, avain):
        solmu = trie.juuri
        for symboli in avain:
            if symboli not in solmu.lapset:
                return False
            solmu = solmu.lapset[symboli]
        return solmu.paate
    
    assert haku(trie, melodia1)
    assert haku(trie, melodia2)
    assert haku(trie, melodia3)
    assert not haku(trie, (60, 62))

    print("testit ok")

if __name__ == "__main__":
    testaa_melodia_trie()