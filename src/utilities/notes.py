from typing import List

VALKOISET_NUOTIT = set(list("ABCDEFG"))
                       
def normalisioi_nuottisekvenssi(sekvenssi: List[str]) -> List[str]:
    """ Normalisoi nuottisekvenssi siten, että se sisältää vain val valkoiset nuotit """
    if not sekvenssi:
        return []
    out = []
    for nuotti in sekvenssi.upper(): # Muutetaan nuotit isoiksi kirjaimiksi  
        if nuotti in VALKOISET_NUOTIT:  # Tarkistetaan, että nuotti on valkoinen nuotti 
            out.append(nuotti)   
    return out

def onko_c_maj_am_asteikko(sekvenssi: List[str]) -> bool:
    """ Tarkistaa, onko nuottisekvenssi C-duuri tai A-molli asteikolla """
    if not sekvenssi:
        return False
    return all(nuotti in VALKOISET_NUOTIT for nuotti in sekvenssi)

def jaa_ikkunoihin(sekvenssi: List[str], n: int):
    """ Jaa nuottisekvenssi ikkunoihin """
    if n <= 0 or len(sekvenssi) < n:
        return []
    return [tuple(sekvenssi[i:i+n]) for i in range(len(sekvenssi) - n + 1)]       