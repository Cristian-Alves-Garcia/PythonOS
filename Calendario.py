import tkinter as tk
import calendar
from datetime import datetime

hoje = datetime.now()
ano = hoje.year
mes = hoje.month
dia_hoje = hoje.day

nome_mes = calendar.month_name[mes]

janela = tk.Tk()
janela.title("Calendário DEBUG")
janela.geometry("500x350")

label = tk.Label(
    janela,
    text=f"{nome_mes} {ano}",
    font=("Arial", 16, "bold")
)
label.pack(pady=5)

sub = tk.Label(
    janela,
    text="Calendário simples em modo texto",
    font=("Arial", 9)
)
sub.pack()

texto = tk.Text(janela, font=("Courier", 12))
texto.pack(expand=True, fill="both", padx=10, pady=10)

texto.insert(tk.END, "Seg  Ter  Qua  Qui  Sex  Sab  Dom\n")
texto.insert(tk.END, "--------------------------------\n")

cal = calendar.monthcalendar(ano, mes)

for semana in cal:
    linha = ""
    for dia in semana:
        if dia == 0:
            linha += " --   "
        else:
            if dia == dia_hoje:
                linha += f"[{dia:>2}]  "
            else:
                linha += f" {dia:>2}   "
    texto.insert(tk.END, linha + "\n")

texto.insert(
    tk.END,
    f"\nHoje: {dia_hoje}/{mes}/{ano} (marcado com [ ])\n"
)

texto.config(state="disabled")
janela.mainloop()
