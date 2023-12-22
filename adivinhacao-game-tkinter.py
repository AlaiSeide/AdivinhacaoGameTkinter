import random
import tkinter

# Criando a janela principal
janela = tkinter.Tk()
janela.title("Jogo de Adivinhação")
janela.geometry('400x200')
janela.resizable(False, False)

# Gerando um valor aleatório entre 1 e 5
valor_aleatorio = random.randint(1, 5)

# Função para lidar com o chute do jogador
def Chute():
    chute = int(entry.get())
    if chute > valor_aleatorio:
        resultado.config(text='Chute é maior que o valor gerado')
    elif chute < valor_aleatorio:
        resultado.config(text='Chute é menor que o valor gerado')
    else:
        resultado.config(text='PARABÉNS! Você acertou.')

# Configurando a entrada do usuário
entry = tkinter.Entry(janela)
entry.pack()

# Configurando o botão de chute
botao = tkinter.Button(janela, text="Chutar", command=Chute)
botao.pack()

# Configurando a exibição do resultado
resultado = tkinter.Label(janela, text=" ")
resultado.pack()

# Iniciando o loop da interface gráfica
janela.mainloop()
