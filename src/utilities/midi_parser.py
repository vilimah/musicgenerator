from utilities.midi_utils import nuotit_midista, pitch_to_nuotti
import os
import traceback

C_DUURI_MOD12 = {0, 2, 4, 5, 7, 9, 11}


def on_c_duuri(pitch_lista, sallittu_poikkeama=0.0): 
    if not pitch_lista:
        return False
    poikkeavat = [pitch for pitch in pitch_lista if (pitch % 12) not in C_DUURI_MOD12]
    osuus = len(poikkeavat) / len(pitch_lista)
    print(f"Poikkeavia nuotteja: {len(poikkeavat)} / {len(pitch_lista)} ({osuus*100:.2f}%)")
    return osuus <= sallittu_poikkeama

def lue_midi_kansiosta(kansio):
    """ palauttaa listan tupleja jossa on nuotti ja sen kesto """

    kaikkien_nuotit = []
    for nimi in os.listdir(kansio):
        if nimi.lower().endswith((".mid", ".midi")):
            polku = os.path.join(kansio, nimi)
            try:
                nuotit = nuotit_midista(polku)
                if not nuotit:
                    continue
                pitch_lista = [p for p, _, _ in nuotit]

                # Testaa tiedoston nuottien skaalaa ja tulosta debug-tietoa
                print(f"Tiedosto {nimi}: {len(pitch_lista)} nuottia, poikkeavia: {sum((pitch % 12) not in C_DUURI_MOD12 for pitch in pitch_lista)}")

                if on_c_duuri(pitch_lista, sallittu_poikkeama=0):
                    nimetyt = [(pitch_to_nuotti(p), kesto) for p, kesto, _ in nuotit]
                    kaikkien_nuotit.extend(nimetyt)
                else:
                    print(f"Tiedosto {nimi} ei ole C-duurissa, ohitetaan.")
            except Exception as e:
                print(f"Error tiedostossa {nimi}: {e}")
                traceback.print_exc()
                continue

    return kaikkien_nuotit
