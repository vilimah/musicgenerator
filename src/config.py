from dataclasses import dataclass

@dataclass
class AppConfig:
    """ Käyttöliittymää varten oletusarvot syötteille"""
    default_degree: int = 4
    default_length: int = 64
    default_tempo_bpm: int = 120
    default_ticks_per_beat: int = 480