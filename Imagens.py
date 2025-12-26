import tkinter as tk
import os

root = tk.Tk()
root.title("Gerenciador de Arquivos")
root.geometry("600x400")

# TÍTULO VISÍVEL
titulo = tk.Label(
    root,
    text="GERENCIADOR DE ARQUIVOS (DEBUG)",
    font=("Arial", 14, "bold")
)
titulo.pack(pady=5)

# CAMINHO ATUAL
caminho = os.getcwd()

path_label = tk.Label(
    root,
    text=f"Pasta atual:\n{caminho}",
    font=("Arial", 9)
)
path_label.pack(pady=5)

# LISTA CRUA
lista = tk.Listbox(root, font=("Courier", 10))
lista.pack(expand=True, fill="both", padx=10, pady=10)

# POPULA MANUALMENTE
lista.insert(tk.END, "=== CONTEÚDO DA PASTA ===")

try:
    for item in os.listdir(caminho):
        if os.path.isdir(item):
            lista.insert(tk.END, f"[DIR]  {item}")
        else:
            lista.insert(tk.END, f"       {item}")
except Exception as e:
    lista.insert(tk.END, f"ERRO: {e}")

# TEXTO DE DEBUG
rodape = tk.Label(
    root,
    text="o codigo está terrivel volto concertar otra hora perdi a paciencia.",
    font=("Arial", 8)
)
rodape.pack(pady=5)

root.mainloop()
