import tkinter as tk
from tkinter import filedialog, messagebox

arquivo_atual = None
modificado = False

# janela
janela = tk.Tk()
janela.title("Bloco de Notas")
janela.geometry("600x400")

# texto
texto = tk.Text(janela, wrap="word")
texto.pack(expand=True, fill="both")

# scrollbar
scroll = tk.Scrollbar(texto)
scroll.pack(side="right", fill="y")
scroll.config(command=texto.yview)
texto.config(yscrollcommand=scroll.set)

# marca modificação (qualquer tecla já conta)
def marcou_modificacao(event=None):
    global modificado
    modificado = True
    if "*" not in janela.title():
        janela.title("* Bloco de Notas")

texto.bind("<Key>", marcou_modificacao)

# funções
def novo():
    global arquivo_atual, modificado
    if not pode_fechar():
        return
    texto.delete(1.0, tk.END)
    arquivo_atual = None
    modificado = False
    janela.title("Bloco de Notas")

def abrir():
    global arquivo_atual, modificado
    if not pode_fechar():
        return
    arquivo = filedialog.askopenfilename(
        filetypes=[("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*")]
    )
    if arquivo:
        texto.delete(1.0, tk.END)
        with open(arquivo, "r", encoding="utf-8") as f:
            texto.insert(tk.END, f.read())
        arquivo_atual = arquivo
        modificado = False
        janela.title(f"Bloco de Notas - {arquivo}")

def salvar():
    global arquivo_atual, modificado
    if arquivo_atual:
        with open(arquivo_atual, "w", encoding="utf-8") as f:
            f.write(texto.get(1.0, tk.END))
        modificado = False
        janela.title(f"Bloco de Notas - {arquivo_atual}")
    else:
        salvar_como()

def salvar_como():
    global arquivo_atual
    arquivo = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*")]
    )
    if arquivo:
        arquivo_atual = arquivo
        salvar()

def pode_fechar():
    if modificado:
        resposta = messagebox.askyesnocancel(
            "Aviso",
            "Você tem alterações não salvas.\nDeseja salvar antes de sair?"
        )
        if resposta is None:   # cancelar
            return False
        if resposta:          # sim
            salvar()
        return True
    return True

def sair():
    if pode_fechar():
        janela.destroy()

# menu
menu = tk.Menu(janela)
janela.config(menu=menu)

menu_arquivo = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Arquivo", menu=menu_arquivo)

menu_arquivo.add_command(label="Novo", command=novo)
menu_arquivo.add_command(label="Abrir", command=abrir)
menu_arquivo.add_command(label="Salvar", command=salvar)
menu_arquivo.add_separator()
menu_arquivo.add_command(label="Sair", command=sair)

# intercepta fechar pela janela
janela.protocol("WM_DELETE_WINDOW", sair)

janela.mainloop()
