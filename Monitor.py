import tkinter as tk
import psutil
from datetime import datetime

# tenta GPU, mas não depende dela
try:
    import GPUtil
    GPU_OK = True
except:
    GPU_OK = False

root = tk.Tk()
root.title("Monitor de Sistema")
root.geometry("400x350")

# TÍTULO
tk.Label(
    root,
    text="MONITOR DE SISTEMA",
    font=("Arial", 14, "bold")
).pack(pady=5)

# TEXTO PRINCIPAL
texto = tk.Text(root, font=("Courier", 10))
texto.pack(expand=True, fill="both", padx=10, pady=10)

def atualizar():
    texto.config(state="normal")
    texto.delete("1.0", tk.END)

    # HORA
    texto.insert(tk.END, f"Atualizado em: {datetime.now().strftime('%H:%M:%S')}\n")
    texto.insert(tk.END, "-" * 40 + "\n")

    # CPU
    cpu = psutil.cpu_percent(interval=None)
    texto.insert(tk.END, f"CPU: {cpu}%\n")

    # RAM
    ram = psutil.virtual_memory()
    texto.insert(
        tk.END,
        f"RAM: {ram.used // (1024**2)} MB / {ram.total // (1024**2)} MB ({ram.percent}%)\n"
    )

    # SWAP
    swap = psutil.swap_memory()
    texto.insert(
        tk.END,
        f"SWAP: {swap.used // (1024**2)} MB / {swap.total // (1024**2)} MB ({swap.percent}%)\n"
    )

    # DISCO
    disco = psutil.disk_usage("/")
    texto.insert(
        tk.END,
        f"DISCO: {disco.used // (1024**3)} GB / {disco.total // (1024**3)} GB ({disco.percent}%)\n"
    )

    # BATERIA
    bateria = psutil.sensors_battery()
    if bateria:
        texto.insert(
            tk.END,
            f"BATERIA: {bateria.percent}% {'(Carregando)' if bateria.power_plugged else '(Usando)'}\n"
        )
    else:
        texto.insert(tk.END, "BATERIA: indisponível\n")

    # GPU (opcional)
    if GPU_OK:
        gpus = GPUtil.getGPUs()
        if gpus:
            gpu = gpus[0]
            texto.insert(
                tk.END,
                f"GPU: {gpu.name} | Uso: {int(gpu.load*100)}% | VRAM: {int(gpu.memoryUsed)}MB/{int(gpu.memoryTotal)}MB\n"
            )
        else:
            texto.insert(tk.END, "GPU: não detectada\n")
    else:
        texto.insert(tk.END, "GPU: indisponível (sem suporte)\n")

    texto.insert(tk.END, "-" * 40 + "\n")
    texto.insert(tk.END, "Modo texto • Estável")

    texto.config(state="disabled")

    # atualiza a cada 1 segundo
    root.after(1000, atualizar)

# INICIA
atualizar()
root.mainloop()
