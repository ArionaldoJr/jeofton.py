import tkinter as tk

# Função para avaliar a expressão
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

# Criando a janela principal
janela = tk.Tk()
janela.title("Calculadora Jeofton")
janela.geometry("300x400")
janela.resizable(False, False)

# Campo de entrada
entrada = tk.Entry(janela, font=("Arial", 20), borderwidth=2, relief="ridge", justify="right")
entrada.pack(padx=10, pady=10, fill="both")

# Layout dos botões
botoes = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', 'C', '=', '+']
]

# Criar os botões na interface
for linha in botoes:
    frame = tk.Frame(janela)
    frame.pack(expand=True, fill="both")
    for item in linha:
        botao = tk.Button(frame, text=item, font=("Arial", 18), command=lambda x=item: clicar(x))
        botao.pack(side="left", expand=True, fill="both")

# Inicia a interface
janela.mainloop()