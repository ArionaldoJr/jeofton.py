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
            adicionar_historico(f"{atual} = {resultado}")
        except Exception:
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, "Erro")
            adicionar_historico(f"{atual} = Erro")
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

# Adicionar entrada ao histórico
def adicionar_historico(texto):
    historico_text.config(state=tk.NORMAL)
    historico_text.insert(tk.END, texto + "\n")
    historico_text.see(tk.END)
    historico_text.config(state=tk.DISABLED)

# Limpar histórico
def limpar_historico():
    historico_text.config(state=tk.NORMAL)
    historico_text.delete("1.0", tk.END)
    historico_text.config(state=tk.DISABLED)

# Janela principal
janela = tk.Tk()
janela.title("Calculadora Jeofton")
janela.geometry("320x550")
janela.configure(bg="#1e1e1e")
janela.bind("<Key>", tecla_pressionada)

# Visor da calculadora
entrada = tk.Entry(janela, font=("Arial", 24), bd=10, relief=tk.FLAT,
                   justify="right", bg="#252525", fg="white")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Botões da calculadora
botoes = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C", "", "", ""]
]

for i, linha in enumerate(botoes, start=1):
    for j, texto in enumerate(linha):
        if texto == "":
            continue
        cor_botao = "#3a3a3a" if texto not in ["=", "C"] else "#007acc" if texto == "=" else "#cc0000"
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

# Título do histórico
titulo_hist = tk.Label(janela, text="Histórico", font=("Arial", 14, "bold"),
                       bg="#1e1e1e", fg="white")
titulo_hist.grid(row=6, column=0, columnspan=4, pady=(10, 0))

# Área destacada do histórico
frame_hist = tk.Frame(janela, bg="#1e1e1e", highlightbackground="white", highlightthickness=1)
frame_hist.grid(row=7, column=0, columnspan=4, sticky="nsew", padx=10, pady=(5, 5))

historico_text = tk.Text(frame_hist, height=6, bg="#1e1e1e", fg="white",
                         font=("Arial", 12), relief=tk.FLAT, state=tk.DISABLED, wrap="none")
scrollbar = tk.Scrollbar(frame_hist, command=historico_text.yview)
historico_text.config(yscrollcommand=scrollbar.set)

historico_text.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Botão para limpar histórico
btn_limpar_hist = tk.Button(
    janela,
    text="Limpar Histórico",
    font=("Arial", 12),
    fg="white",
    bg="#cc0000",
    relief=tk.FLAT,
    command=limpar_historico
)
btn_limpar_hist.grid(row=8, column=0, columnspan=4, padx=10, pady=(0, 10), sticky="nsew")

# Responsividade
total_linhas = 9
total_colunas = 4

for i in range(total_linhas):
    janela.grid_rowconfigure(i, weight=1)
for j in range(total_colunas):
    janela.grid_columnconfigure(j, weight=1)

# Iniciar a janela
janela.mainloop()
