from mido import MidiFile

def nuotit_midista(tiedosto):
    """ Pohja tiedoston lukua varten
    """
    midi = MidiFile(tiedosto) 
    nuotit = [] # lista nuoteille

    for raita in midi.tracks:
        aika = 0
        for viesti in raita:
            aika += viesti.time

            if viesti.type == "note_on" and viesti.velocity > 0: # lisää nuotteihin vain nuotit jotka ovat päällä
                nuotit.append((viesti.note, aika)) # lisää korkeuden ja ajan
                aika = 0

    return nuotit