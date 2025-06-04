import tkinter as tk

def clicar(botao):
    atual = entrada.get()
    if botao == "=":
        try:
            resultado = eval(atual)
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, str(resultado))
        except:
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, "Erro")
    elif botao == "C":
        entrada.delete(0, tk.END)
    else:
        entrada.insert(tk.END, botao)

def tecla(evento):
    tecla_pressionada = evento.char
    if tecla_pressionada in "0123456789+-*/.":
        entrada.insert(tk.END, tecla_pressionada)
    elif tecla_pressionada == '\r':  # Enter
        clicar("=")
    elif evento.keysym == 'BackSpace':
        entrada.delete(len(entrada.get())-1, tk.END)
    elif evento.keysym == 'Escape':
        clicar("C")

# Janela principal
janela = tk.Tk()
janela.title("Calculadora Jeofton")
janela.geometry("300x400")
janela.resizable(False, False)

# Entrada
entrada = tk.Entry(janela, font=("Arial", 20), borderwidth=2, relief="ridge", justify="right")
entrada.pack(padx=10, pady=10, fill="both")
entrada.focus_set()  # Foco no campo de entrada

# Vincula o teclado à função tecla()
janela.bind("<Key>", tecla)

# Botões
botoes = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', 'C', '=', '+']
]

for linha in botoes:
    frame = tk.Frame(janela)
    frame.pack(expand=True, fill="both")
    for item in linha:
        botao = tk.Button(frame, text=item, font=("Arial", 18), command=lambda x=item: clicar(x))
        botao.pack(side="left", expand=True, fill="both")

# Loop principal
janela.mainloop()
