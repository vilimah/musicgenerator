import os
from typing import List, Optional

def midi_tiedosto_in(hakemisto: str):
    """ Midi-tiedosto hakemistosta """
    for juuri, _, tiedostot in os.walk(hakemisto):
        for t in tiedostot:
            if t.lower().endswith(".mid") or t.lower().endswith(".midi"):
                yield os.path.join(juuri, t)

def melodia_midista(path: str) -> Optional[List[str]]:
    """ Melodian saanti midista.
        Tämä palauttaa listan nuoteista jotka ovat C-duurissa.
                                                                """
    try:
        import mido
    except Exception:
        return None
    
    nuotit = []
    try:
        mid = mido.MidiFile(path)
        for raita in mid.tracks:
            for viesti in raita:
                if viesti.type == "note_on" and viesti.velocity > 0:
                    pitch = viesti.note % 12
                    kirjain = pitch_kirjaimeksi(pitch)
                    nuotit.append(kirjain)
    except Exception:
        return None
    return nuotit

PITCH_KIRJAIMIKSI  = {0: "C", 1: "C#", 2: "D", 3: "D#", 4: "E", 5: "F",
                       6: "F#", 7: "G", 8: "G#", 9: "A", 10: "A#", 11: "B"}

def pitch_kirjaimeksi(pitch_luokka: int) -> str:
    return PITCH_KIRJAIMIKSI.get(pitch_luokka % 12, "C")

def exporttaa_midiksi(path: str, sek, tempo: int = 120, ticks_per_beat: int = 480):
    try:
        import mido
    except Exception as e:
        raise RuntimeError("Midin exporttaaminen vaatii mido kirjaston") from e
    
    mid = mido.MidiFile(ticks_per_beat=ticks_per_beat)
    raita = mido.MidiTrack()
    mid.tracks.append(raita)

    tempo = mido.bpm2tempo(tempo)
    raita.append(mido.MetaMessage("set_tempo", tempo=tempo, time=0))

    for i in sek:
        if isinstance(i, tuple):
            ch, dur = i
        else:
            ch, dur = i, 0.25
        note = kirjain_midiksi(ch, 5)
        ticks = int(ticks * (dur / 0.25)) # 1/4 nuotti
        raita.append(mido.Message("note_on", note=note, velocity=64, time=0))
        raita.append(mido.Message("note_off", note=note, velocity=64, time=ticks))
    
    mid.save(path)

KIRJAIN_MIDIKSI = {"C": 60, "D": 62, "E": 64, "F": 65, "G": 67, "A": 69, "B": 71}

def kirjain_midiksi(kirjain: str, oktaavi: int = 5) -> int:
    pohja = KIRJAIN_MIDIKSI.get(kirjain.upper(), 60)
    nykyinen_oktaavi = 4
    erotus = (oktaavi - nykyinen_oktaavi) * 12
    return pohja + erotus