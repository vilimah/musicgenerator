import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.model.markov import MarkovGen

class TestiMarkovGen(unittest.TestCase):
    """ Markovin ketjun generoinnin testaus """
    def testi_opetus_ja_gen(self):
        """ testataan kovakoodatulla datalla """
        data = [60,62,64,65,67,69,71]
        generaattori = MarkovGen(aste=2)
        generaattori.opetus(data)
        tulos = generaattori.generointi(pituus=7)

        self.assertEqual(len(tulos), 7)

        for nuotti in tulos:
            self.assertIn(nuotti, data)

    def testi_tyhja_malli(self):
        """ testataan tyhjällä datalla """
        generaattori = MarkovGen()
        tulos = generaattori.generointi(pituus=7)
        self.assertEqual(tulos, [])

if __name__ == "__main__":
    unittest.main()