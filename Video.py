import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Player de Vídeo Simples")
root.geometry("640x480")

# TÍTULO
titulo = tk.Label(
    root,
    text="PLAYER DE VÍDEO (SIMPLÃO)",
    font=("Arial", 14, "bold")
)
titulo.pack(pady=5)

# LABEL DO VÍDEO
video_label = tk.Label(root, text="Nenhum vídeo carregado")
video_label.pack(expand=True)

cap = None
frame_tk = None

def abrir_video():
    global cap

    arquivo = filedialog.askopenfilename(
        title="Escolha um vídeo",
        filetypes=[
            ("Vídeos", "*.mp4 *.avi *.mkv *.mov"),
            ("Todos os arquivos", "*.*")
        ]
    )

    if not arquivo:
        return

    if cap:
        cap.release()

    cap = cv2.VideoCapture(arquivo)
    tocar()

def tocar():
    global frame_tk

    if not cap or not cap.isOpened():
        return

    ret, frame = cap.read()
    if not ret:
        cap.release()
        return

    # converte BGR -> RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # redimensiona
    frame = cv2.resize(frame, (600, 360))

    img = Image.fromarray(frame)
    frame_tk = ImageTk.PhotoImage(img)

    video_label.config(image=frame_tk, text="")

    # controla FPS (~30)
    root.after(33, tocar)

# BOTÃO
btn = tk.Button(root, text="Abrir Vídeo", command=abrir_video)
btn.pack(pady=5)

# RODAPÉ
rodape = tk.Label(
    root,
    text="Funcional até certo ponto.",
    font=("Arial", 8)
)
rodape.pack(pady=5)

root.mainloop()
