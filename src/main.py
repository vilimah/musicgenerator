import tkinter as tk
from tkinter import filedialog, messagebox
from utilities.midi_parser import lue_midi_kansiosta
from model.markov import rakenna_trie, generoi_triella
from utilities.midi_utils import exporttaa_midi, generoi_tiedostonimi, nuotti_nimi_to_midi

class MusicGeneratorApp:
    def __init__(self, root):
        self.root = root
        root.title("Melodiageneraattori")

        # Valinta midi-kansiolle
        self.kansio_label = tk.Label(root, text="Valitse MIDI-kansio:")
        self.kansio_label.pack()
        self.kansio_button = tk.Button(root, text="Selaa", command=self.valitse_kansio)
        self.kansio_button.pack()

        # Aste
        self.aste_label = tk.Label(root, text="Aste (esim. 3):")
        self.aste_label.pack()
        self.aste_entry = tk.Entry(root)
        self.aste_entry.insert(0, "3")
        self.aste_entry.pack()

        # Melodian pituus
        self.pituus_label = tk.Label(root, text="Melodian pituus:")
        self.pituus_label.pack()
        self.pituus_entry = tk.Entry(root)
        self.pituus_entry.insert(0, "50")
        self.pituus_entry.pack()

        # BPM
        self.bpm_label = tk.Label(root, text="Tempo (BPM):")
        self.bpm_label.pack()
        self.bpm_entry = tk.Entry(root)
        self.bpm_entry.insert(0, "120")
        self.bpm_entry.pack()

        # Generoi-painike
        self.generoi_button = tk.Button(root, text="Generoi melodia", command=self.generate_melody)
        self.generoi_button.pack()

        self.kansio = None

    def valitse_kansio(self):
        self.kansio = filedialog.askdirectory()
        if self.kansio:
            self.kansio_label.config(text=f"Valittu kansio: {self.kansio}")

    def generate_melody(self):
        if not self.kansio:
            messagebox.showerror("Virhe", "Valitse ensin MIDI-kansio")
            return
        try:
            aste = int(self.aste_entry.get())
            pituus = int(self.pituus_entry.get())
            bpm = int(self.bpm_entry.get())
        except ValueError:
            messagebox.showerror("Virhe", "Syötä numerot oikein")
            return

        try:
            opetusdata = lue_midi_kansiosta(self.kansio)
            if not opetusdata:
                messagebox.showerror("Virhe", "Opetusdata on tyhjä tai ei löytynyt sopivia MIDI-tiedostoja")
                return

            trie = rakenna_trie(opetusdata, aste=aste)
            melodia = generoi_triella(trie, pituus=pituus, aste=aste)

            # Muunnetaan nuotit MIDI-numeroiksi oletusoktavilla 4
            melodia_midi = []
            for nuotti in melodia:
                if isinstance(nuotti, tuple) and len(nuotti) == 3:
                    # Jos melodia-tuplat on (pitch, kesto, delta) ja pitch on int, käytä sellaisenaan
                    pitch, kesto, delta = nuotti
                    if not isinstance(pitch, int):
                        pitch = nuotti_nimi_to_midi(pitch)
                    melodia_midi.append((pitch, kesto, delta))
                else:
                    # Jos pelkkä nuotti nimi (esim. 'C'), anna oletusarvot kesto ja delta
                    pitch = nuotti_nimi_to_midi(nuotti)
                    melodia_midi.append((pitch, 0.5, 0))  # oletuskesto ja delta

            tiedosto = generoi_tiedostonimi(self.kansio)
            exporttaa_midi(melodia_midi, tiedosto, bpm)
            messagebox.showinfo("Valmis", f"Melodia tallennettu tiedostoon:\n{tiedosto}")

        except Exception as e:
            messagebox.showerror("Virhe", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = MusicGeneratorApp(root)l
    root.mainloop()
