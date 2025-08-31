# Toteutusdokumentti

Tässä dokumentissa käy ilmi ohjelman yleisrakenne, saavutetut aika- ja tilavaativuudet, työn mahdollisista puutteista tai parannusehdotuksista, kielimallien käytöstä
sekä olennaiset lähteet.

## Ohjelman yleisrakenne

Ohjelman rakenne toimii siten, että model-kansion sisältä löytyy toimivuus eli Markovin-ketjujen generointi (markov.py) , Trie-tietorakenne (trie.py) ja trainer.py
Utilities-kansio sisältää notes.py, jossa on C-majorin tarkistus.
Io-kansio sisältää midi- ja tekstitiedostojen käsittelyn.
gui.py sisältää ohjelman käyttöliittymän ja sinne ohjataan näistä edellisistä tiedostoista toimminta.
Lopuksi ohjelma ajetaan app.py tiedostossa.

## Aikavaativuudet



### Trie-rakenne
Insertissä sekvenssi pituus on m ja aste n ja jokaisesta m-n ikkunasta lisätään solmu trieen. Ikkunnan lisäämiseen käytetty aika on O(n) askelta. Tällöin koko aikavaatimus on O((m-n)*n).

Haku eli next_distribution käy läpi ikkunat ajassa O(n), jossa jokainen symboli (nuotti) käydään läpi.

Kaikki ikunat funktiossa aikavaatimus on O(k^n), jossa k on eri symbolien (nuottien) määrä.

### Markov-gen
Sample laskurista funktio käy läpi Counterin avaimet ja tällöin aikavaatimus on O(n).

Nuotin keston arvonta (samplen kesto) käyttää random kirjastosta choices arvontaa ja tämän aikavaatimuus riippuu painojen määrästä eli se on O(1) tässä tapauksessa.

Triellä generoinnissa generoidaan m määrä nuotteja, jossa jokaisessa muodostetaan ikuna n. Sen jälkeen arvotaan seuraava nuotti o. Tällöin aikavaatimukseksi muodostuu O(m*(n+o)) 

## Puutteet ja parannukset
Melodian nuottien pituuksien generointiin voisi olla järkevämpi toteutus.
Opetusdatassa on vaihtoehtoja, mutta niissä ei ole mitään genre jakoa.
Ohjelmaan voisi lisätä sävellajin valitsimen. Tällä hetkellä se generoi melodian vain C-duurissa/A-mollissa.

## Kielimallien käyttö
ChatGPT:tä käytetty alussa suunnitteluun, että pääseen alkuun. Kysyin, miten tulisi aloittaa se auttoi minut etsimään tietoa oikeista paikoista. Kysyin myös, mistä tulisi etsiä sopivaa opetusdataa projektiani varten. ChatGPT:tä käytetty myös virheiden etsimiseen koodistani. 
Projekti otti vähän takapakkia viikolla 5, joten ChatGPT:ltä kysytty koottu-ideointi vielä rakenteesta, sillä sen hahmottaminen oli tässä kohtaa hukassa. ChatGPT:llä myös generoitu käyttöliittymä projektia varten.

Visual Studio Code:ssa käytetty funktioiden kommentoinnin apuna Copilot-tekoälytyökalua.

## Lähteet
- Trie wikipedia-artikkeli: https://en.wikipedia.org/wiki/Trie?utm_source=chatgpt.com
- Markov chain wikipedia-artikkeli: https://en.wikipedia.org/wiki/Markov_chain
- Pygame midi -kirjasto: https://www.pygame.org/docs/ref/midi.html
- https://docs.python.org/3/library/unittest.html
- Mido -kirjasto https://mido.readthedocs.io/en/stable/
