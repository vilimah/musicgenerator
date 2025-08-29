import os
import random
import tkinter as tk
from tkinter import filedialog, messagebox
from src.config import AppConfig
from src.utilities.notes import onko_c_maj_am_asteikko, normalisioi_nuottisekvenssi
from src.io.text_io import lue_tekstina, kirjoita_tekstina
from src.io.midi_io import midi_tiedosto_in, melodia_midista, exporttaa_midiksi
from src.model.trainer import Trainer

CFG = AppConfig()

def seuraava_tiedosto(hakemisto: str, pohja: str) -> tuple[str, str]:
    """ Luo seuraavan tiedoston nimen hakemistoon """
    i = 1
    while True:
        txt_path = os.path.join(hakemisto, f"{pohja}_{i}.txt")
        mid_path = os.path.join(hakemisto, f"{pohja}_{i}.mid")
        if not os.path.exists(txt_path) and not os.path.exists(mid_path):
            return txt_path, mid_path
        i += 1

def run_app():
    root = tk.Tk()
    root.title("MelGen – Trie/Markov")

    # Vars
    degree_var = tk.StringVar(value=str(CFG.default_degree))
    length_var = tk.StringVar(value=str(CFG.default_length))
    tempo_var = tk.StringVar(value=str(CFG.default_tempo_bpm))
    seed_var = tk.StringVar(value="")
    data_dir_var = tk.StringVar(value="")

    # Layout
    pad = {"padx": 6, "pady": 6}
    frm = tk.Frame(root)
    frm.pack(fill="both", expand=True, **pad)

    tk.Label(frm, text="Aste (n-gram)").grid(row=0, column=0, sticky="e", **pad)
    tk.Entry(frm, textvariable=degree_var, width=10).grid(row=0, column=1, sticky="w", **pad)

    tk.Label(frm, text="Pituus (nuottia)").grid(row=1, column=0, sticky="e", **pad)
    tk.Entry(frm, textvariable=length_var, width=10).grid(row=1, column=1, sticky="w", **pad)

    tk.Label(frm, text="Tempo (BPM)").grid(row=2, column=0, sticky="e", **pad)
    tk.Entry(frm, textvariable=tempo_var, width=10).grid(row=2, column=1, sticky="w", **pad)

    #tk.Label(frm, text="Siemen (A–G, vapaaehtoinen)").grid(row=3, column=0, sticky="e", **pad)
    #tk.Entry(frm, textvariable=seed_var, width=30).grid(row=3, column=1, sticky="w", **pad)

    tk.Label(frm, text="Opetusdatan kansio").grid(row=4, column=0, sticky="e", **pad)
    tk.Entry(frm, textvariable=data_dir_var, width=40).grid(row=4, column=1, sticky="w", **pad)

    def choose_dir():
        d = filedialog.askdirectory(title="Valitse opetusdatan kansio")
        if d:
            data_dir_var.set(d)
    tk.Button(frm, text="Selaa…", command=choose_dir).grid(row=4, column=2, **pad)

    out_txt = tk.Text(frm, height=8, width=72)
    out_txt.grid(row=6, column=0, columnspan=3, **pad)

    def run_training_and_generate():
        try:
            degree = int(degree_var.get())
            length = int(length_var.get())
            tempo = int(tempo_var.get())
            if degree < 1 or length < 1:
                raise ValueError("Asteen ja pituuden täytyy olla vähintään 1.")
        except Exception as e:
            messagebox.showerror("Virhe", f"Syötearvo(t) virheellisiä: {e}")
            return

        data_dir = data_dir_var.get().strip()
        if not data_dir or not os.path.isdir(data_dir):
            messagebox.showerror("Virhe", "Valitse olemassa oleva opetusdatan kansio.")
            return

        # Lataa txt- ja midi-melodiat
        melodies = []
        txts = lue_tekstina(data_dir)
        for m in txts:
            seq = normalisioi_nuottisekvenssi(m)
            if seq and onko_c_maj_am_asteikko(seq):
                melodies.append(seq)

        for mf in midi_tiedosto_in(data_dir):
            seq = melodia_midista(mf)
            if seq and onko_c_maj_am_asteikko(seq):
                melodies.append(seq)

        if not melodies:
            messagebox.showwarning("Ei dataa", "C-duuri/A-molli -kelpoista opetusdataa ei löytynyt.")
            return

        # Valmistele Trainer ja trie
        trainer = Trainer()
        for seq in melodies:
            trainer.lisaa_sekvenssi(seq)
        trainer.sequences = melodies
        trie = trainer.rakenna_trie()

        # Generointi
        seed = normalisioi_nuottisekvenssi(seed_var.get())
        if seed and len(seed) >= degree:
            start = seed[:degree]
        else:
            start = random.choice(trainer.sequences)[:degree]

        generated = trainer.generoi(trie=trie, pituus=length, aloitus=start)

        # Erotetaan nuotit ja kestot
        notes_only = [note for note, duration in generated]


# Tulostus tekstikenttään
        gen_str = " ".join(notes_only)
        out_txt.delete("1.0", tk.END)
        out_txt.insert(tk.END, f"Generoitu melodia ({len(generated)} nuottia):\n{gen_str}\n")

        # Tallennus
        save_dir = filedialog.askdirectory(title="Valitse kansio tallennukselle (txt+mid)")
        if save_dir:
            txt_path, mid_path = seuraava_tiedosto(save_dir, "melodia")
            kirjoita_tekstina(txt_path, notes_only)

            try:
                exporttaa_midiksi(mid_path, generated, tempo=tempo)
            except Exception as e:
                messagebox.showwarning("MIDI-vienti epäonnistui", f"Syynä: {e}")

            messagebox.showinfo("Valmis", f"Tallennettu:\n- {txt_path}\n- {mid_path}")

    tk.Button(frm, text="Kouluta + Generoi", command=run_training_and_generate).grid(row=5, column=0, columnspan=3, **pad)

    root.mainloop()