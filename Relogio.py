import tkinter as tk
from datetime import datetime

root = tk.Tk()
root.title("Relógio Simples")
root.geometry("300x150")

# TÍTULO
titulo = tk.Label(
    root,
    text="RELÓGIO",
    font=("Arial", 14, "bold")
)
titulo.pack(pady=5)

# HORA
hora_label = tk.Label(
    root,
    text="--:--:--",
    font=("Courier", 24)
)
hora_label.pack()

# DATA
data_label = tk.Label(
    root,
    text="--/--/----",
    font=("Courier", 12)
)
data_label.pack()

def atualizar():
    agora = datetime.now()
    hora_label.config(text=agora.strftime("%H:%M:%S"))
    data_label.config(text=agora.strftime("%d/%m/%Y"))
    root.after(1000, atualizar)

# INICIA
atualizar()

root.mainloop()
