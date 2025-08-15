import unittest
from collections import Counter
from src.model.trie import Trie, TrieSolmu

class TestTrie(unittest.TestCase):
    """ Testit Trie-luokalle """

    def test_insertti_ja_next_distribution(self):
        """ Testaa insertti ja next_distribution metodit """
        trie = Trie(aste=2)
        sekvenssi = ["A", "B", "C", "D", "E"]
        trie.insertti(sekvenssi)
        ikkuna = ["A", "B"]
        dist = trie.next_distribution(ikkuna)
        self.assertEqual(dist, Counter({"C": 1}))
        dist2 = trie.next_distribution(["B", "C"])
        self.assertEqual(dist2, Counter({"D": 1}))

    def test_insertti_liian_lyhyt(self):
        """ Testaa insertti kun sekvenssi on liian lyhyt """
        trie = Trie(aste=3)
        sekvenssi = ["A", "B", "C"]
        trie.insertti(sekvenssi)
        self.assertEqual(trie.kaikki_ikkunat(), []) # ei ikkunoita koska sekvenssi on liian lyhyt

    def test_node_for_luo_false(self):
        """ Testaa _node_for metodia luo=False """
        trie = Trie(aste=2)
        sekvenssi = ["A", "B", "C"]
        trie.insertti(sekvenssi)
        # olemassa oleva ikkuna
        solmu = trie._node_for(["A", "B"], luo=False)
        self.assertIsNotNone(solmu)
        # ikkuna joka ei ole olemassa
        solmu2 = trie._node_for(["X", "Y"], luo=False)
        self.assertIsNone(solmu2)
    
    def test_node_for_luo_true(self):
        """ Testaa _node_for metodia luo=True """
        trie = Trie(aste=2)
        solmu = trie._node_for(["A", "B"], luo=True)
        self.assertIsInstance(solmu, TrieSolmu)

    def test_next_distribution_tyhja(self):
        """ Testaa next_distribution kun ikkuna on tyhjä """
        trie = Trie(aste=2)
        dist = trie.next_distribution(["A", "B"])
        self.assertEqual(dist, Counter())

    def test_kaikki_ikkunat(self):
        """ Testaa kaikkien ikkunoiden palautus """
        trie = Trie(aste=2)
        sekvenssi = ["A", "B", "C", "D"]
        trie.insertti(sekvenssi)
        ikkunat = trie.kaikki_ikkunat()
        self.assertIn(("A", "B"), ikkunat)
        self.assertIn(("B", "C"), ikkunat)
        self.assertEqual(len(ikkunat), 2)

if __name__ == "__main__":
    unittest.main()