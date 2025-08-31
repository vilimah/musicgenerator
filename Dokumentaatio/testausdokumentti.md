# Testausdokumentti

Projektista löytyy testit trielle, markoville ja trainerille.

## Testauksen raportti

### Markovin testaus
* Trielle asetettu kovat arvot dataksi: ("A", "B"): Counter({"C": 5, "D": 3}), ("B", "C"): Counter({"A": 2, "D": 4}). 


## Kattavuusraportti

# Testausraportti


| Tiedosto                     | Rivejä (Stmts) | Puuttuvat (Miss) | Kattavuus (Cover) | Puuttuvat rivit (Missing) |
|-------------------------------|----------------|------------------|-------------------|----------------------------|
| src/__init__.py               | 0              | 0                | 100%              | –                          |
| src/io/__init__.py            | 0              | 0                | 100%              | –                          |
| src/model/__init__.py         | 0              | 0                | 100%              | –                          |
| src/model/markov.py           | 36             | 2                | 94%               | 26, 50                     |
| src/model/trainer.py          | 35             | 2                | 94%               | 35, 42                     |
| src/model/trie.py             | 45             | 0                | 100%              | –                          |
| src/utilities/__init__.py     | 0              | 0                | 100%              | –                          |
| tests/__init__.py             | 0              | 0                | 100%              | –                          |
| tests/test_markov.py          | 40             | 1                | 98%               | 64                         |
| tests/test_trainer.py         | 50             | 1                | 98%               | 77                         |
| tests/test_trie.py            | 44             | 1                | 98%               | 61                         |
| **TOTAL**                     | **250**        | **7**            | **97%**           |                            |