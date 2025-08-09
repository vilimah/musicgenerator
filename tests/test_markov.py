import unittest
from src.model.markov import rakenna_trie, generoi_triella, painotettu_valinta
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

class TestiMarkovGen(unittest.TestCase):
    def setUp(self):
        self.opetusdata = ["60", "62", "64", "65", "64", "69", "71", "67", "69", "71", "72", "74", "60", "62", "64", "65", "64", "69", "71", "67", "69", "71", "72", "74"]
        self.aste = 3
        self.trie = rakenna_trie(self.opetusdata, aste=self.aste)
        print("\n[setUp] Trie rakennettu syötteellä:", self.opetusdata)
        print("[setUp] Aste:", self.aste)

    def test_rakenna_trie(self):
        print("[test_rakenna_trie] Trie juuren lapset:", list(self.trie.juuri.lapset.keys()))
        self.assertIsNotNone(self.trie.juuri.lapset)
        self.assertGreater(len(self.trie.juuri.lapset), 0)

    def test_painotettu_valinta(self):
        vaihtoehdot = {"60": 2, "62": 1}
        print("[test_painotettu_valinta] Vaihtoehdot:", vaihtoehdot)
        valinnat = [painotettu_valinta(vaihtoehdot) for _ in range(100)]
        print("[test_painotettu_valinta] Valinnat (20 kpl):", valinnat)
        self.assertIn("60", valinnat)
        self.assertIn("62", valinnat)

    def test_generoi_triella_pituus(self):
        melodia = generoi_triella(self.trie, pituus=10, aste=self.aste)
        print("[test_generoi_triella_pituus] Generoitu melodia:", melodia)
        self.assertGreaterEqual(len(melodia), self.aste)
        self.assertLessEqual(len(melodia), 10)

    def test_generoi_triella(self):
        melodia = generoi_triella(self.trie, pituus=10, aste=self.aste)
        print("[test_generoi_triella] Generoitu melodia:", melodia)
        for nuotti in melodia:
            self.assertIn(nuotti, self.opetusdata)


if __name__ == "__main__":
    unittest.main()