import os
from typing import Iterable, Tuple, Union, List, Optional
from mido import MidiFile, MidiTrack, Message, MetaMessage, bpm2tempo
from src.config import AppConfig

CFG = AppConfig()

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

PITCH_MIDIKSI = {
    "C": 60, "C#": 61, "D": 62, "D#": 63, "E": 64, "F": 65, "F#": 66,
    "G": 67, "G#": 68, "A": 69, "A#": 70, "B": 71
}

def pitch_kirjaimeksi(pitch_luokka: int) -> str:
    PITCH_KIRJAIMIKSI  = {0: "C", 1: "C#", 2: "D", 3: "D#", 4: "E", 5: "F",
                       6: "F#", 7: "G", 8: "G#", 9: "A", 10: "A#", 11: "B"}
    return PITCH_KIRJAIMIKSI.get(pitch_luokka % 12, "C")

def exporttaa_midiksi(path: str, melodia: Iterable[Union[str, Tuple[str, float]]], tempo: int = 120, ticks_per_beat: int = None, channel: int = 0, program: int = 0) -> None:
    if ticks_per_beat is None:
        ticks_per_beat = CFG.default_ticks_per_beat
    mid = MidiFile(ticks_per_beat=ticks_per_beat)
    track = MidiTrack()
    mid.tracks.append(track)

    track.append(MetaMessage("set_tempo", tempo=bpm2tempo(tempo), time=0))
    track.append(Message("program_change", program=program, channel=channel, time=0))

    for item in melodia:
        if isinstance(item, tuple) and len(item) == 2:
            kirjain, kesto = item   # erotellaan nuotti ja kesto
        elif isinstance(item, str):
            kirjain, kesto = item, 0.25  # oletuskesto
        else:
            raise ValueError(f"Virheellinen melodiaelementti: {item}")

        nuotti_summa = _nuotti_midiksi(kirjain)  # nyt kirjain on string
        delta_ticks = _kesto_tikeiksi(float(kesto), ticks_per_beat)
        
        
        track.append(Message("note_on", note=nuotti_summa, velocity=64, time=0, channel=channel))
        track.append(Message("note_off", note=nuotti_summa, velocity=64, time=delta_ticks, channel=channel))

    mid.save(path)

KIRJAIN_MIDIKSI = {"C": 60, "D": 62, "E": 64, "F": 65, "G": 67, "A": 69, "B": 71}

def _nuotti_midiksi(nuotti: str, oletus_oktaavi: int = 4) -> int:
    s = nuotti.strip()
    i = len(s) - 1

    while i >= 0 and s[i].isdigit():
        i -= 1
    pitch = s[:i + 1].strip().upper()
    oktaavi_str = s[i + 1:].strip()
    oktaavi = int(oktaavi_str) if oktaavi_str else oletus_oktaavi
    if pitch not in PITCH_MIDIKSI:
        raise ValueError(f"Tuntematon nuotti: {nuotti}")
    
    midi_arvo = 12 * (oktaavi - 3) + PITCH_MIDIKSI[pitch]

    midi_arvo = max(0, min(127, midi_arvo))  # MIDI-arvojen rajoitus
    return midi_arvo

def _kesto_tikeiksi(kesto: float, ticks_per_beat: int) -> int:
    """ Muuntaa keston tikeiksi """
    if abs(kesto - 0.25) < 1e-9 or abs(kesto - 0.5) < 1e-9 or abs(kesto - 1.0) < 1e-9:
        beats = kesto * 4.0
    else:
        beats = kesto

    ticks = int(round(max(1, beats * ticks_per_beat)))
    return ticks
