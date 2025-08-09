import os
from mido import MidiFile, MidiTrack, Message, MetaMessage, bpm2tempo

# Modulo 12 arvot ja nuotinimet
nuotti_arvot = {
    0: "C",
    1: "C#",
    2: "D",
    3: "D#",
    4: "E",
    5: "F",
    6: "F#",
    7: "G",
    8: "G#",
    9: "A",
    10: "A#",
    11: "B"
}

def pitch_to_nuotti(pitch):
    if not isinstance(pitch, int):
        raise TypeError(f"pitch_to_nuotti: pitch ei ole int: {pitch} ({type(pitch)})")
    key = pitch % 12
    if key not in nuotti_arvot:
        raise ValueError(f"pitch_to_nuotti: modulo 12 arvo {key} ei ole nuotti_arvot:ssa")
    return nuotti_arvot[key]

def normalize_nuotti(nimi: str) -> str:
    """Korvaa esim. 'Bb' -> 'A#', 'Db' -> 'C#' jne."""
    korvaus = {
        "Bb": "A#",
        "Db": "C#",
        "Eb": "D#",
        "Gb": "F#",
        "Ab": "G#"
    }
    return korvaus.get(nimi, nimi)

def nuotti_nimi_to_midi(nimi, oktaavi=4):
    # Jos nimi on tuple, ota siitä ensimmäinen alkio
    if isinstance(nimi, tuple):
        nimi = nimi[0]
    nimi = nimi.strip()
    nimi = normalize_nuotti(nimi)
    inv_nuotit = {v: k for k, v in nuotti_arvot.items()}
    base = inv_nuotit.get(nimi)
    if base is None:
        raise ValueError(f"Nuotti tuntematon: {nimi}")
    return base + (oktaavi + 1) * 12

def nuotit_midista(tiedosto):
    midi = MidiFile(tiedosto)
    nuotit = []  # pitch, kesto, aloitusaika
    aika = 0
    pitch = None
    aloitus_aika = None

    for viesti in midi:
        aika += viesti.time
        if viesti.type == "note_on" and viesti.velocity > 0:
            pitch = viesti.note
            aloitus_aika = aika
        elif (viesti.type == "note_off") or (viesti.type == "note_on" and viesti.velocity == 0):
            if pitch is not None and aloitus_aika is not None:
                kesto = aika - aloitus_aika
                nuotit.append((pitch, round(kesto, 4), round(aloitus_aika, 4)))
                pitch = None
                aloitus_aika = None

    nuotit.sort(key=lambda n: n[2])  # aloitusajan mukaan
    tulos = []
    viimeinen_aloitus = 0.0
    for pitch, kesto, aloitus in nuotit:
        delta = round(aloitus - viimeinen_aloitus, 4)
        tulos.append((pitch, round(kesto, 4), delta))
        viimeinen_aloitus = aloitus
    return tulos

def exporttaa_midi(melodia, tiedosto, bpm):
    midi = MidiFile()
    raita = MidiTrack()
    midi.tracks.append(raita)

    tempo = bpm2tempo(bpm)
    raita.append(MetaMessage("set_tempo", tempo=tempo, time=0))

    ticks_per_beat = midi.ticks_per_beat

    for pitch, kesto, delta in melodia:
        if not isinstance(pitch, int):
            raise TypeError(f"exporttaa_midi: pitch ei ole int: {pitch} ({type(pitch)})")
        delta_ticks = int(delta * ticks_per_beat)
        kesto_ticks = int(kesto * ticks_per_beat)

        raita.append(Message("note_on", note=pitch, velocity=100, time=delta_ticks))
        raita.append(Message("note_off", note=pitch, velocity=100, time=kesto_ticks))

    midi.save(tiedosto)

def generoi_tiedostonimi(kansio, nimi="melodia", paate=".mid"):
    i = 1
    while True:
        koko_nimi = f"{nimi}_{i}{paate}"
        polku = os.path.join(kansio, koko_nimi)
        if not os.path.exists(polku):
            return polku
        i += 1
