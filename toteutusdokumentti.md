# Toteutusdokumentti

Tässä dokumentissa käy ilmi ohjelman yleisrakenne, saavutetut aika- ja tilavaativuudet, työn mahdollisista puutteista tai parannusehdotuksista, kielimallien käytöstä
sekä olennaiset lähteet.

## Ohjelman yleisrakenne

Ohjelman rakenne toimii siten, että model-kansion sisältä löytyy toimivuus eli Markovin-ketjujen generointi (markov.py) , Trie-tietorakenne (trie.py) ja itse generaattori (generaattori.py). 
Utilities sisältää löytyy midi-tiedostojen läpikäyvä funktio. Ja sitten on main.py, jolla pystyy generoimaan melodioita. Tällä hetkellä generator.py tuntuu vielä vähän hyödyttömältä, sillä loin
sen ennen main.py:tä, mutta sitä voi käyttää paikalliseen generointiin tai toisaalta voisin integroida sen toiminnan main.py käytettäväksi, tai
jopa poistaa kokonaan. Data-kansiosta löytyy opetusdata.

## Aika- ja tilavaativuudet

## Puutteet ja parannukset
Koodissa on generator.py, joka oli hetkellisesti käytössä generoimassa melodioita, mutta nyt se on käytännössä turha ja puutteellinen. Joko siirrän toiminnan main.py:stä generator.py:lle tai sitten poistan sen kokonaan. Puuttuu vielä testauksia ja aika- ja tilavaativuuden tekeminen.

## Kielimallien käyttö
ChatGPT:tä käytetty alussa suunnitteluun, että pääseen alkuun. Kysyin, miten tulisi aloittaa se auttoi minut etsimään tietoa oikeista paikoista. Kysyin myös, mistä tulisi etsiä sopivaa opetusdataa projektiani varten. ChatGPT:tä käytetty myös virheiden etsimiseen koodistani.

## Lähteet
- Trie wikipedia-artikkeli: https://en.wikipedia.org/wiki/Trie?utm_source=chatgpt.com
- Markov chain wikipedia-artikkeli: https://en.wikipedia.org/wiki/Markov_chain
