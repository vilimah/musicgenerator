# Toteutusdokumentti

Tässä dokumentissa käy ilmi ohjelman yleisrakenne, saavutetut aika- ja tilavaativuudet, työn mahdollisista puutteista tai parannusehdotuksista, kielimallien käytöstä
sekä olennaiset lähteet.

## Ohjelman yleisrakenne

Ohjelman rakenne toimii siten, että model-kansion sisältä löytyy toimivuus eli Markovin-ketjujen generointi (markov.py) , Trie-tietorakenne (trie.py) ja itse generaattori (generaattori.py). 
Utilities sisältää löytyy midi-tiedostojen läpikäyvä funktio. Ja sitten on main.py, jolla pystyy generoimaan melodioita. Tällä hetkellä generator.py tuntuu vielä vähän hyödyttömältä, sillä loin
sen ennen main.py:tä, mutta sitä voi käyttää paikalliseen generointiin tai toisaalta voisin integroida sen toiminnan main.py käytettäväksi, tai
jopa poistaa kokonaan. Data-kansiosta löytyy opetusdata.

## Aika- ja tilavaativuudet

### Trie-rakenne
Insertissä sekvenssi pituus on m ja aste n ja jokaisesta m-n ikkunasta lisätään solmu trieen. Ikkunnan lisäämiseen käytetty aika on O(n) askelta. Tällöin koko aikavaatimus on O((m-n)*n).

Haku eli next_distribution käy läpi ikkunat ajassa O(n), jossa jokainen symboli (nuotti) käydään läpi.

Kaikki ikunat funktiossa aikavaatimus on O(k^n), jossa k on eri symbolien (nuottien) määrä.

### Markov-gen


## Puutteet ja parannukset
Nyt rakennuspalikat alkavat olemaan kohdillaan, mutta vähän vielä epäilen koodissani olevan pieni ongelma. Se generoi kyllä satunnaisia melodioita, mutta tein sellaisen ratkaisun, että jos ei löydetä jollakin x asteella enää uutta nuottia ja generoiminen päättyy, niin se toistaa sitten tätä melodiaa. Ongelmana on, että tuntuu, että se tuottaa hyvin lyhyitä melodioita tällä hetkellä (pienilläkin asteilla), jotka sitten toistaa itseään. 

Lisäksi en ole vielä löytänyt mitään järkevää keinoa nuottien pituuksien generoimiseen. Tällä hetkellä se arpoo kokonuotin, puolinuotin ja neljännesosa nuotin väliltä, että mikä niistä asetetaan. Tähän myös liittyy ongelma, että jos ohjelma tuottaa melodioita edellä mainitulla tavalla eli se alkaa toistamaan itseään, niin se toistaa melodiaa epäsatunnaisten baarien välillä. Esimerkiksi olisi siis järkevää, että melodia toistuu tasa-baarien välillä (esim. 4 baarin välein), mutta melodiani ovat luokkaa 2,5 baaria tai jotain vastaavaa.

## Kielimallien käyttö
ChatGPT:tä käytetty alussa suunnitteluun, että pääseen alkuun. Kysyin, miten tulisi aloittaa se auttoi minut etsimään tietoa oikeista paikoista. Kysyin myös, mistä tulisi etsiä sopivaa opetusdataa projektiani varten. ChatGPT:tä käytetty myös virheiden etsimiseen koodistani. 
Projekti otti vähän takapakkia viikolla 5, joten ChatGPT:ltä kysytty koottu ideointi vielä rakenteesta, sillä sen hahmottaminen oli tässä kohtaa hukassa. ChatGPT:llä myös generoitu käyttöliittymä projektia varten.

Visual Studio Code:ssa käytetty funktioiden kommentoinnin apuna Copilot-tekoälytyökalua.

## Lähteet
- Trie wikipedia-artikkeli: https://en.wikipedia.org/wiki/Trie?utm_source=chatgpt.com
- Markov chain wikipedia-artikkeli: https://en.wikipedia.org/wiki/Markov_chain
- Pygame midi -kirjasto: https://www.pygame.org/docs/ref/midi.html
- https://docs.python.org/3/library/unittest.html
