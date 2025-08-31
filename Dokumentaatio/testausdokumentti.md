# Testausdokumentti

Projektista löytyy testit trielle, markoville ja trainerille.

## Testauksen raportti

### Markovin testaus
Trielle asetettu kovat arvot dataksi: ("A", "B"): Counter({"C": 5, "D": 3}), ("B", "C"): Counter({"A": 2, "D": 4}). 
#### Arvoilla testattu funktioita:
* sample_laskurista, jossa arvotaan seuraava elementti Counterista
* sample_kesto, joka palauttaa satunnaisen keston nuotille (arvoina: neljäsosa-, puoli- ja kokonuotti)
* generoi_triella, jossa annettu aloitus ["A", "B"] ja aste = 2
* generoi_triella, mutta aloitus on tuntematon, kuten "X" ja "Y"

### Trien testaus
#### Testatut funktiot
* insertti_ja_next_distribution, jossa valmis sekvenssi on A,B,C,D,E ja aste = 2 ja ikkuna A, B
* insertti_liian_lyhyt, jossa sekvenssi on A, B, C. Testataan sitä, kun insertti on liian lyhyt
* _node_for_luo_false, jossa testataan solmun palautusta ikkunalle kun luo=false
 _node_for_luo_true, jossa testataan solmun palautustusta ikkunalle kun luo=true
* next_distribution_tyhja, jossa testataan toimivuutta kun Counter on tyhjä
* next_distribution_kaikki_ikkunat, jossa taas testataan kaikilla ikkunoilla. Sekvenssi on A, B, C, D ja kaikki ikkunat haetaan trielta. 

### Trainerin testaus
Valmiiksi koodatut nuotti sekvenssit: 
["C", "D", "E", "F", "G", "A", "B", "C"],
["A", "B", "C", "D", "E", "F", "G", "A"],
["G", "F", "E", "D", "C", "B", "A", "G"]
#### Testatut funktiot
* lisaa_sekvenssi, jossa testataan aloitusikkunan lisäystä nuottisekvenssiin. Sekvenssi C, D, E, F, G ja lisää ikkunan C, D, E ja lisäksi lisää aloitukset laskuriin +1
* fit, jossa testataan trie-rakenteen rakentamista annetusta listasta. Käyttää aste=2 ja valmiiksi annettuja nuotti sekvenssejä.
* rakenna_trie, käytännössä sama kuin edellinen, mutta testataan vielä, että funktio toimii triessa
* painotettu_aloitus, jossa testataan painotettu aloitus valmiiksi koodatuilla nuotti sekvensseillä ja aste=2
* generoi, jossa käytetään aste=2, nuotti sekvenssejä, aloitus C, D ja pituus 5 ja generoi näillä tiedoilla melodian
* lataa_opetusdata, testaa tässä tapauksessa valmiiksi koodatuilla nuotti sekvensseillä

## Testausraportti


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