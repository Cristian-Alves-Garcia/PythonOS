import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Abridor de Imagem Simples")
root.geometry("600x500")

# TÍTULO
titulo = tk.Label(
    root,
    text="ABRIDOR DE IMAGEM (SIMPLÃO)",
    font=("Arial", 14, "bold")
)
titulo.pack(pady=5)

# LABEL DA IMAGEM
img_label = tk.Label(root, text="Nenhuma imagem carregada")
img_label.pack(expand=True)

# referência global (IMPORTANTE no Tkinter)
img_tk = None

def abrir_imagem():
    global img_tk

    arquivo = filedialog.askopenfilename(
        title="Escolha uma imagem",
        filetypes=[
            ("Imagens", "*.png *.jpg *.jpeg *.bmp *.gif"),
            ("Todos os arquivos", "*.*")
        ]
    )

    if not arquivo:
        return

    # abre imagem
    img = Image.open(arquivo)

    # redimensiona para caber
    largura_max = 550
    altura_max = 400
    img.thumbnail((largura_max, altura_max))

    img_tk = ImageTk.PhotoImage(img)

    img_label.config(image=img_tk, text="")

# BOTÃO
btn = tk.Button(root, text="Abrir Imagem", command=abrir_imagem)
btn.pack(pady=5)

# RODAPÉ
rodape = tk.Label(
    root,
    text="correção de erros outra hora.",
    font=("Arial", 8)
)
rodape.pack(pady=5)

root.mainloop()
