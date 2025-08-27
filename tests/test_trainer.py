import unittest
from src.model.trainer import Trainer
from src.model.trie import Trie

NUOTTI_SEKVENSSIT = [
    ["C", "D", "E", "F", "G", "A", "B", "C"],
    ["A", "B", "C", "D", "E", "F", "G", "A"],
    ["G", "F", "E", "D", "C", "B", "A", "G"]
    ]

class TestTrainer(unittest.TestCase):
    """ Testit Trainer-luokalle """

    def test_lisaa_sekvenssi(self):
        """ Testaa lisaa_sekvenssi metodi """
        trainer = Trainer(aste=3)
        sekvenssi = ["C", "D", "E", "F", "G"]
        trainer.lisaa_sekvenssi(sekvenssi)

        self.assertIn(("C", "D", "E"), trainer.aloitukset)
        self.assertEqual(trainer.aloitukset_laskuri[("C", "D", "E")], 1)

    def test_fit(self):
        """ Testaa fit metodi """
        trainer = Trainer(aste=2)
        trie = trainer.fit(NUOTTI_SEKVENSSIT)

        self.assertIsInstance(trie, Trie)
        self.assertEqual(trie.aste, 2)

    def test_rakenna_trie(self):
        """ Testaa rakenna_trie metodi """
        trainer = Trainer(aste=2)
        trainer.lataa_opetusdata(NUOTTI_SEKVENSSIT)
        trie = trainer.rakenna_trie()

        self.assertIsInstance(trie, Trie)
        self.assertEqual(trie.aste, 2)

    def test_painotettu_aloitus(self):
        """ Testaa painotettu_aloitus metodi """
        trainer = Trainer(aste=2)
        trainer.lataa_opetusdata(NUOTTI_SEKVENSSIT)
        
        aloitus = trainer.painotettu_aloitus()
        self.assertEqual(len(aloitus), 2)
        self.assertIn(tuple(aloitus), trainer.aloitukset)

    def test_generoi(self):
        """ Testaa generoi metodi """
        trainer = Trainer(aste=2)
        trainer.lataa_opetusdata(NUOTTI_SEKVENSSIT)
        trie = trainer.rakenna_trie()

        aloitus = ["C", "D"]
        pituus = 5
        melodia = trainer.generoi(trie, pituus, aloitus)

        self.assertEqual(len(melodia), pituus)
        for nuotti, kesto in melodia:
            self.assertIsInstance(nuotti, str)
            self.assertIsInstance(kesto, float)

    def test_lataa_opetusdata(self):
        """ Testaa lataa_opetusdata metodi """
        trainer = Trainer(aste=3)
        trainer.lataa_opetusdata(NUOTTI_SEKVENSSIT)

        self.assertEqual(len(trainer.sekvenssit), len(NUOTTI_SEKVENSSIT))
        self.assertEqual(len(trainer.aloitukset), len(NUOTTI_SEKVENSSIT))
        for sekvenssi in NUOTTI_SEKVENSSIT:
            aloitus = tuple(sekvenssi[:3])
            self.assertIn(aloitus, trainer.aloitukset)
            self.assertEqual(trainer.aloitukset_laskuri[aloitus], 1)

if __name__ == "__main__":
    unittest.main()