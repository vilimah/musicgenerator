import os
from utilities.midi_utils import nuotit_midista
from model.markov import MarkovGen

def main():
    sekvenssi = []
    midi_kansio = os.path.join("src", "data", "opetusdata", "midi")

    for tiedosto in os.listdir(midi_kansio):
        if tiedosto.endswith(".mid"):
            polku = os.path.join(midi_kansio, tiedosto)
            print(f"Luetaan: {polku}")
            sekvenssi.extend(nuotit_midista(polku))

    print(f"Ladattu yhteensä {len(sekvenssi)} nuottitapahtumaa.")

    generaattori = MarkovGen(aste=2)
    generaattori.opetus(sekvenssi)

    generoitu = generaattori.generointi(pituus=30)
    print("Generoitu melodia:")
    for pitch, kesto, delta in generoitu:
        print(f"Nuotti: {pitch}, kesto: {kesto}, tauko ennen seuraavaa: {delta}")

if __name__ == "__main__":
    main()
    
