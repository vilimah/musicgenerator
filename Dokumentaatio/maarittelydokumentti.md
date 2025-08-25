# Määrittelydokumentti

Käytän tässä projektissa Pythonia ja se on myös ainoa ohjelmointikieli, jota pystyn arvioimaan sujuvasti.

## Aiheesta ja sen toteutuksesta 

Valitsin aiheeksi musiikin generoiminen. Tässä projektissa tulen hyödyntämään erilaisia python-kirjastoja ja midi-kirjastoa. Tulen käyttämään trie-tietorakennetta ja markovin ketjuja.

Ongelmat, joita tulen ratkaisemaan liittyvät melodioiden luontiin, johon taas liittyy oikea sävelaste, rytmi ja korkeus. Hyödynnän koneoppimista löytämään yleisiä sääntöjä opetusdatasta.

Ohjelman tulisi toimia siten, että käyttäjältä kysytään aste ja kuinka pitkän kappaleen haluaa generoitavan ja hän voi valita millaista opetusdataa käytetään. 

Tässä ohjelmassa käytettävä trie-tietorakenne on hyvin tehokas, sillä sen search, insert ja delete operaatiot toimivat ajassa O(n) ja tilavaatimus on samoin O(n). Markovin ketjuista en vielä saanut tätä tietoa.


## Lähteet
Käytän projektissa seuraavia lähteitä:
- Trie wikipedia-artikkeli: https://en.wikipedia.org/wiki/Trie?utm_source=chatgpt.com
- Markov chain wikipedia-artikkeli: https://en.wikipedia.org/wiki/Markov_chain
