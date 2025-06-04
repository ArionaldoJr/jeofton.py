import tkinter as tk
from tkinter import ttk

# Função o visor
def clicar(botao):
    atual = entrada.get()
    if botao == "C":
        entrada.delete(0, tk.END)
    elif botao == "=":
        try:
            resultado = eval(atual)
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, str(resultado))
        except Exception:
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, "Erro")
    else:
        entrada.insert(tk.END, botao)

# Função para teclado
def tecla_pressionada(event):
    tecla = event.keysym

    if tecla in "0123456789":
        entrada.insert(tk.END, tecla)
    elif tecla in ["plus", "minus", "asterisk", "slash", "period"]:
        simbolos = {
            "plus": "+",
            "minus": "-",
            "asterisk": "*",
            "slash": "/",
            "period": "."
        }
        entrada.insert(tk.END, simbolos[tecla])
    elif tecla == "Return":  # Enter
        clicar("=")
    elif tecla == "BackSpace":
        entrada.delete(len(entrada.get()) - 1, tk.END)
    elif tecla == "Escape":  # ESC para limpar
        clicar("C")

# Janela principal
janela = tk.Tk()
janela.title("Calculadora Professor Jeofton")
janela.geometry("300x400")
janela.configure(bg="#1a053e")

# Suporte ao teclado
janela.bind("<Key>", tecla_pressionada)

# Estilo
style = ttk.Style()
style.configure("TButton", font=("Arial", 14), padding=10)

# Visor da calculadora
entrada = tk.Entry(janela, font=("Arial", 24), bd=10, relief=tk.FLAT, justify="right", bg="#178BBD", fg="white")
entrada.pack(pady=20, padx=10, fill="x")

# Botões da calculadora
botoes = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]

frame_botoes = tk.Frame(janela, bg="#1a053e")
frame_botoes.pack()

for linha in botoes:
    linha_frame = tk.Frame(frame_botoes, bg="#0e3e68")
    linha_frame.pack(side="top", fill="x")
    for texto in linha:
        cor_botao = "#1e1e4b" if texto not in ["=", "C"] else "#007acc" if texto == "=" else "#cc0000"
        botao = tk.Button(
            linha_frame,
            text=texto,
            width=5,
            height=2,
            font=("Arial", 16),
            fg="white",
            bg=cor_botao,
            relief=tk.FLAT,
            command=lambda t=texto: clicar(t)
        )
        botao.pack(side="left", expand=True, fill="both", padx=3, pady=3)

# Iniciar a janela
janela.mainloop()