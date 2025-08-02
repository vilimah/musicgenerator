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

## Kielimallien käyttö

## Lähteet

