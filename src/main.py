import os
from utilities.midi_utils import nuotit_midista
from model.markov import MarkovGen

def main():
    """ Lataa opetusdatan, kouluttaa Markov-ketjut ja generoi melodian.
        Tämä vielä ei ole täysin toimintakunnossa funktion valmiiseen versioon nähden.
        Ei pysty vielä kuuntelemaan melodiaa """
    sekvenssi = [] # nuotti tapahtumat lisätään tänne
    midi_kansio = os.path.join("src", "data", "opetusdata", "midi") # midi kansion polku

    for tiedosto in os.listdir(midi_kansio): # Käy läpi midi kansiossa olevat midit
        if tiedosto.endswith(".mid"): # varmistus että on midi tiedosto
            polku = os.path.join(midi_kansio, tiedosto) # polku
            #print(f"Luetaan: {polku}")
            sekvenssi.extend(nuotit_midista(polku)) # lukee nuotit ja lisää ne sekvenssiin

    print(f"Ladattu yhteensä {len(sekvenssi)} nuottitapahtumaa.")

    generaattori = MarkovGen(aste=2) # Markovin ketjujen generointi
    generaattori.opetus(sekvenssi) # opetusdatan käyttö

    generoitu = generaattori.generointi(pituus=30) # tämä generoi nyt 30 nuotin sarjan
    print("Generoitu melodia:")
    # tässä ei ole vielä haluttua toimintaa sillä nyt vain printtaa mitkä nuotit generoitiin ja
    # lisäinfoo siihen liittyen
    for pitch, kesto, delta in generoitu:
        print(f"Nuotti: {pitch}, kesto: {kesto}, tauko ennen seuraavaa: {delta}") 

if __name__ == "__main__":
    main()
    
