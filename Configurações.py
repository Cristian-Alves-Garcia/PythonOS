import tkinter as tk

root = tk.Tk()
root.title("pythonOS - Configurações")
root.geometry("800x500")

# ---------- CONTAINER ----------
container = tk.Frame(root)
container.pack(fill="both", expand=True)

menu = tk.Frame(container, width=200, bg="#dddddd")
menu.pack(side="left", fill="y")

conteudo = tk.Frame(container)
conteudo.pack(side="right", fill="both", expand=True)

# ---------- TÍTULO ----------
tk.Label(
    menu,
    text="CONFIGURAÇÕES",
    font=("Arial", 12, "bold"),
    bg="#dddddd"
).pack(pady=10)

# ---------- ÁREA DE TEXTO ----------
texto = tk.Text(
    conteudo,
    font=("Courier", 10),
    wrap="word"
)
texto.pack(fill="both", expand=True, padx=10, pady=10)

def escrever(titulo, linhas):
    texto.delete("1.0", tk.END)
    texto.insert(tk.END, f"{titulo}\n")
    texto.insert(tk.END, "-" * len(titulo) + "\n\n")
    for l in linhas:
        texto.insert(tk.END, f"- {l}\n")

# ---------- CATEGORIAS ----------
def geral():
    escrever("GERAL", [
        "Idioma do sistema",
        "Tema (claro / escuro)",
        "Inicialização de aplicativos",
        "Atualizações do sistema",
        "Sobre o pythonOS"
    ])

def sistema():
    escrever("SISTEMA", [
        "Armazenamento e discos",
        "Processos em execução",
        "Energia e bateria",
        "Desempenho (CPU / RAM)",
        "Logs do sistema"
    ])

def rede():
    escrever("REDE", [
        "Status da conexão",
        "Wi-Fi (abrir configurações)",
        "Ethernet",
        "Proxy",
        "VPN"
    ])

def tela():
    escrever("TELA", [
        "Resolução",
        "Escala",
        "Brilho",
        "Fontes",
        "Modo tela cheia"
    ])

def apps():
    escrever("APLICATIVOS", [
        "Aplicativos instalados",
        "Aplicativos padrão",
        "Permissões",
        "Associações de arquivos",
        "Limpeza de cache"
    ])

def privacidade():
    escrever("PRIVACIDADE", [
        "Permissões (câmera, microfone)",
        "Histórico de atividades",
        "Localização",
        "Telemetria",
        "Limpeza de dados"
    ])

# ---------- BOTÕES ----------
tk.Button(menu, text="Geral", command=geral).pack(fill="x", padx=10, pady=2)
tk.Button(menu, text="Sistema", command=sistema).pack(fill="x", padx=10, pady=2)
tk.Button(menu, text="Rede", command=rede).pack(fill="x", padx=10, pady=2)
tk.Button(menu, text="Tela", command=tela).pack(fill="x", padx=10, pady=2)
tk.Button(menu, text="Aplicativos", command=apps).pack(fill="x", padx=10, pady=2)
tk.Button(menu, text="Privacidade", command=privacidade).pack(fill="x", padx=10, pady=2)

# ---------- TEXTO INICIAL ----------
escrever("CONFIGURAÇÕES", [
    "Selecione uma categoria à esquerda",
    "Este menu é estrutural",
    "As opções ainda não executam ações",
    "Cada item será ligado a funções futuramente"
])

# ---------- RODAPÉ ----------
tk.Label(
    root,
    text="pythonOS • Menu de Configurações (texto puro)",
    font=("Arial", 8)
).pack(pady=3)

root.mainloop()

#EM DESENVOLVIMENTO 
