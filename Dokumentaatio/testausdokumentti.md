# Testausdokumentti

Projektista löytyy testit trielle sekä markoville.

## Testauksen raportti 26.7

Koodin arviointi näyttää tällä hetkellä vielä 6.37/10. 

Testien perusteella Markovin-ketjujen generoinnin testaus on melkein täydellisesti testattu (96% tällä hetkellä), mutta Trie-tietorakenteen testit 
ovat vielä vajaatja kaipaa lisää testejä (tällä hetkellä 31%).
Olen testannut Markovin-ketjuja siten, että se yrittää kovakoodatun opetusdatan perusteella generoida valmiiksi määritetyn pitusta "nuotti sarjaa".
Tämä on vielä vajaa testi siinä mielessä, että testi yrittää tehdä vain tietyn monta nuottia, joka ei useimmiten onnistu säännöistä ja satunnaisuudesta johtuen. 

Trie-tietorakenteeseen tulee vielä rakentaa testit, joka testaa melodian generoimisen ajallisen pituuden. Tällä hetkellä se testaa vain, että se tallentaa
melodiat oikein, tunnistaa melodian ja se ei pidä osittaista melodiaa lopullisena.

| NAME                        | Stmts          | Miss           | Cover             | Missing                       |
|-----------------------------|----------------|----------------|-------------------|-------------------------------|
| src/model/__init__.py       | 0              | 0              | 100%              | –                             |
| src/model/markov.py         | 23             | 1              | 96%               | 32                            |
| src/model/trie.py           | 16             | 11             | 31%               | 5–7, 13, 18–24                |
| src/tests/markov_test.py    | 20             | 1              | 95%               | 30                            |
| src/tests/trie_test.py      | 26             | 20             | 23%               | 13–36, 39                     |
| TOTAL                       | 85             | 33             | 61%               |                               |
