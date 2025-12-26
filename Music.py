import tkinter as tk
from tkinter import filedialog
import pygame
import os

# inicializa pygame
pygame.init()
pygame.mixer.init()

FIM_MUSICA = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(FIM_MUSICA)

playlist = []
musica_atual = 0
pausado = False

# janela
janela = tk.Tk()
janela.title("Play Music Amador")
janela.geometry("420x360")

# música atual
label_musica = tk.Label(janela, text="Nenhuma música tocando")
label_musica.pack(pady=5)

# lista
lista = tk.Listbox(janela)
lista.pack(fill="both", expand=True, padx=10, pady=5)

# -------- funções --------

def adicionar_musicas():
    arquivos = filedialog.askopenfilenames(
        filetypes=[("Músicas", "*.mp3 *.wav")]
    )
    for a in arquivos:
        playlist.append(a)
        lista.insert(tk.END, os.path.basename(a))

def tocar(index=None):
    global musica_atual, pausado
    if not playlist:
        return

    if index is not None:
        musica_atual = index

    pygame.mixer.music.load(playlist[musica_atual])
    pygame.mixer.music.play()
    pausado = False

    nome = os.path.basename(playlist[musica_atual])
    label_musica.config(text=f"Tocando: {nome}")

    lista.selection_clear(0, tk.END)
    lista.selection_set(musica_atual)

def pause():
    global pausado
    if pausado:
        pygame.mixer.music.unpause()
        pausado = False
    else:
        pygame.mixer.music.pause()
        pausado = True

def stop():
    pygame.mixer.music.stop()
    label_musica.config(text="Parado")

def proxima():
    global musica_atual
    if playlist:
        musica_atual = (musica_atual + 1) % len(playlist)
        tocar()

def anterior():
    global musica_atual
    if playlist:
        musica_atual = (musica_atual - 1) % len(playlist)
        tocar()

def duplo_click(event):
    sel = lista.curselection()
    if sel:
        tocar(sel[0])

def volume(valor):
    pygame.mixer.music.set_volume(float(valor) / 100)

# -------- eventos pygame --------

def checar_eventos_pygame():
    for evento in pygame.event.get():
        if evento.type == FIM_MUSICA:
            proxima()
    janela.after(200, checar_eventos_pygame)

lista.bind("<Double-Button-1>", duplo_click)

# -------- botões --------

frame = tk.Frame(janela)
frame.pack(pady=5)

tk.Button(frame, text="Adicionar", command=adicionar_musicas).grid(row=0, column=0, padx=3)
tk.Button(frame, text="Anterior", command=anterior).grid(row=0, column=1, padx=3)
tk.Button(frame, text="Play", command=tocar).grid(row=0, column=2, padx=3)
tk.Button(frame, text="Pause", command=pause).grid(row=0, column=3, padx=3)
tk.Button(frame, text="Stop", command=stop).grid(row=0, column=4, padx=3)
tk.Button(frame, text="Próxima", command=proxima).grid(row=0, column=5, padx=3)

# volume
tk.Label(janela, text="Volume").pack()
slider = tk.Scale(
    janela, from_=0, to=100,
    orient="horizontal",
    command=volume
)
slider.set(70)
slider.pack(fill="x", padx=20)

# iniciar loop de eventos do pygame
checar_eventos_pygame()

janela.mainloop()
