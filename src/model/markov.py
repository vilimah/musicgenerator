import random
from collections import defaultdict

class MarkovGen:
    """ Markovin ketjujen generointi-luokka
    """
    def __init__(self, aste=2): # aste tulee vielä pystyä vaihtamaan inputilla
        self.aste = aste
        self.malli = defaultdict(list)

    def opetus(self, sekvenssi):
        """ Opetus-funktio
        """
        for i in range(len(sekvenssi) - self.aste):
            avain = tuple(sekvenssi[i:i + self.aste]) # lähtien nykyisestä kohdasta, ottaa osajonon
            seuraava = sekvenssi[i + self.aste] # seuraava nuotti
            self.malli[avain].append(seuraava) # tallentaa seuraavan mahdollisen nuotin
            
    def generointi(self, pituus=50): # pituus tulee vielä pystyä vaihtamaan inputilla
        """ Generointi-funktio
        """
        if not self.malli: # varmistaa, että jos mallia ei ole koulutettu niin palauttaa tyhjän listan
            return []
        
        avain = random.choice(list(self.malli.keys())) # satunnainen aloitusnuotti
        output = list(avain) # aloittaa aloitusnuotista

        for _ in range(pituus - self.aste):
            edellinen = tuple(output[-self.aste:]) # katsoo edelliset nuotit eli x astetta 
            seuraavat_nuotit = self.malli.get(edellinen, [])
            if not seuraavat_nuotit: # jos ei löydy niin generointi loppuu
                break 
            output.append(random.choice(seuraavat_nuotit))

        return output

