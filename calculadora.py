import tkinter as tk
from tkinter import ttk

# Função para atualizar o visor
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

# Função para tratar teclas pressionadas
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
    elif tecla == "Return":
        clicar("=")
    elif tecla == "BackSpace":
        entrada.delete(len(entrada.get()) - 1, tk.END)
    elif tecla == "Escape":
        clicar("C")

# Janela principal
janela = tk.Tk()
janela.title("Calculadora Jeofton")
janela.geometry("300x400")
janela.configure(bg="#0a86cd")

# Suporte ao teclado
janela.bind("<Key>", tecla_pressionada)

# Estilo opcional com ttk (pode ser estendido)
style = ttk.Style()
style.configure("TButton", font=("Arial", 14), padding=10)

# Visor da calculadora
entrada = tk.Entry(janela, font=("Arial", 24), bd=10, relief=tk.FLAT,
                   justify="right", bg="#0A0851", fg="white")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

# Botões da calculadora
botoes = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C", "", "", ""]
]

# Criar os botões em uma grade
for i, linha in enumerate(botoes, start=1):
    for j, texto in enumerate(linha):
        if texto == "":
            continue  # pular espaços vazios
        cor_botao = "#060b7b" if texto not in ["=", "C"] else "#007acc" if texto == "=" else "#cc0000"
        botao = tk.Button(
            janela,
            text=texto,
            font=("Arial", 16),
            fg="white",
            bg=cor_botao,
            relief=tk.FLAT,
            command=lambda t=texto: clicar(t)
        )
        botao.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")

# Tornar colunas e linhas responsivas
total_linhas = len(botoes) + 1
total_colunas = 4

for i in range(total_linhas):
    janela.grid_rowconfigure(i, weight=1)
for j in range(total_colunas):
    janela.grid_columnconfigure(j, weight=1)

# Iniciar a janela
janela.mainloop()
