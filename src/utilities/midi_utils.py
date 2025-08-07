import os
from mido import MidiFile, MidiTrack, Message, MetaMessage, bpm2tempo

def nuotit_midista(tiedosto):
    """ Pohja tiedoston lukua varten
    """
    midi = MidiFile(tiedosto) 
    nuotit = [] # tähän lisätään tieto nuotin pitchistä, kestosta ja aloitus ajasta
    aika = 0
    pitch = None
    aloitus_aika = None

    for viesti in midi: # käydään silmukassa läpi midi tiedoston "viestit"
        #print(viesti)
        aika += viesti.time 
        if viesti.type == "note_on" and viesti.velocity > 0: # jos nuotti on päällä ja nuotin kovuus on yli 0 niin sen tiedot otetaan ylös
            pitch = viesti.note 
            aloitus_aika = aika
        elif (viesti.type == "note_off") or (viesti.type == "note_on" and viesti.velocity == 0): # tässä taas 
            if pitch is not None and aloitus_aika is not None:
                kesto = aika - aloitus_aika 
                nuotit.append((pitch, round(kesto, 4), round(aloitus_aika, 4))) 
                pitch = None
                aloitus_aika = None

    # Tässä opetusdatasta hankitaan tieto kauanko nuottien välillä on väliä eli delta aika
    nuotit.sort(key=lambda n: n[2]) # järjestetään nuotit listasta kolmannen kohdan eli aloitusajan mukaan
    tulos = [] # tähän tallennetaan delta ajan tieto pitchin ja keston kanssa
    viimeinen_aloitus = 0.0
    for pitch, kesto, aloitus in nuotit:
        delta = round(aloitus - viimeinen_aloitus, 4)
        tulos.append((pitch, round(kesto, 4), delta))
        viimeinen_aloitus = aloitus
    return tulos


def exporttaa_midi(melodia, tiedosto, bpm):
    """ exporttaa melodian midinä """

    # os.makedirs(os.path.dirname(tiedosto), exist_ok=True) # tämä luo kansion jos ei vielä ole

    midi = MidiFile()
    raita = MidiTrack()
    midi.tracks.append(raita)

    tempo = bpm2tempo(bpm)
    raita.append(MetaMessage("set_tempo", tempo=tempo, time=0))



    ticks_per_beat = midi.ticks_per_beat

    for pitch, kesto, delta in melodia:
        delta_ticks = int(delta * ticks_per_beat)
        kesto_ticks = int(kesto * ticks_per_beat)

        raita.append(Message("note_on", note=pitch, velocity=100, time=delta_ticks))
        raita.append(Message("note_off", note=pitch, velocity=100, time=kesto_ticks))

    midi.save(tiedosto)

def generoi_tiedostonimi(kansio, nimi="melodia", paate=".mid"):
    """ Tämä lisää melodian nimeen aina uuden numeron, ettei se overwritee tiedostoja generoidessa"""
    i = 1
    while True:
        koko_nimi = f"{nimi}_{i}{paate}"
        polku = os.path.join(kansio, koko_nimi)
        if not os.path.exists(polku):
            return polku
        i += 1