import tkinter as tk

# janela principal
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("260x320")
janela.resizable(False, False)

# visor
entrada = tk.Entry(
    janela,
    width=18,
    font=("Arial", 16),
    borderwidth=3,
    relief="sunken",
    justify="right"
)
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# funções
def clicar(valor):
    entrada.insert(tk.END, valor)

def limpar():
    entrada.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, resultado)
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "erro")

# botões
botoes = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for texto, linha, coluna in botoes:
    if texto == "=":
        btn = tk.Button(
            janela, text=texto, width=5, height=2,
            command=calcular
        )
    else:
        btn = tk.Button(
            janela, text=texto, width=5, height=2,
            command=lambda t=texto: clicar(t)
        )
    btn.grid(row=linha, column=coluna, padx=5, pady=5)

# botão limpar
btn_limpar = tk.Button(
    janela, text="C",
    width=22, height=2,
    command=limpar
)
btn_limpar.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

# loop principal
janela.mainloop()
