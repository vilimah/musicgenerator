import unittest
from collections import Counter
from src.model import markov

class MockTrie:
    """ Data trie:tä varten testaukseen """
    def __init__(self, aste):
        self.aste = aste
        self.data = {
            ("A", "B"): Counter({"C": 5, "D": 3}),
            ("B", "C"): Counter({"A": 2, "D": 4})
        }

    def next_distribution(self, ikkuna):
        """ Mock next_distribution metodi """
        return self.data.get(tuple(ikkuna), None)

class TestMarkov(unittest.TestCase):
    """ Testit Markov-luokalle """

    def test_sample_laskurista(self):
        """ Testaa sample_laskurista funktio """
        lasketut = Counter({"A": 5, "B": 3, "C": 2})
        tulos = markov.sample_laskurista(lasketut)
        self.assertIn(tulos, lasketut)
    
    def test_sample_laskurista_tyhjalla(self):
        """ Testaa sample_laskurista tyhjällä laskurilla """
        self.assertIsNone(markov.sample_laskurista(Counter())) 
        self.assertIsNone(markov.sample_laskurista(Counter({"A": 0})))

    def test_sample_kesto(self):
        """ Testaa sample_kesto funktio """
        for _ in range(10):
            k = markov.sample_kesto()
            self.assertIn(k, [0.25, 0.5, 1.0])

    def test_generoi_triella_perus(self):
        """ Testaa generoi_triella funktio perus tapauksessa """
        trie = MockTrie(aste=2)
        aloitus = ["A", "B"]
        pituus = 5
        melodia = markov.generoi_triella(trie, aloitus, pituus)

        self.assertEqual(len(melodia), pituus)

        for nuotti, kesto in melodia:
            self.assertIsInstance(nuotti, str)
            self.assertIsInstance(kesto, float)

    def test_generoi_triella_tuntematon_aloitus(self):
        """ Testaa generoi_triella tuntemattomalla aloituksella """
        trie = MockTrie(aste=2)
        aloitus = ["X", "Y"]
        melodia = markov.generoi_triella(trie, aloitus, 4)

        self.assertEqual(len(melodia), 4)
        for nuotti, kesto in melodia:
            self.assertIsInstance(nuotti, str)
            self.assertIsInstance(kesto, float)


if __name__ == "__main__":
    unittest.main()