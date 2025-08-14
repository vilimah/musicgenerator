import os
from typing import List

def lue_tekstina(hakemisto: str) -> List[str]:
    melodiat = []
    for juuri, _, tiedostot in os.walk(hakemisto):
        for t in tiedostot:
            if t.lower().endswith(".txt"):
                path = os.path.join(juuri, t)
                try:
                    with open(path, "r", encoding="utf-8") as fh:
                        for rivi in fh:
                            rivi = rivi.strip()
                            if rivi:
                                melodiat.append(rivi)
                except Exception:
                    pass
    return melodiat

def kirjoita_tekstina(path: str, sek: List[str]):
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("".join(sek) + "\n")

        