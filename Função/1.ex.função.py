import os

os.system("cls || clear")

# Função sem retorno.
# Deifinindo característica da função. 
def saudacao(nome):
    print(f"Olá {nome}! Bem-vindo ao curso de DS!")

#def disciplina(materia):
    #print(f"A sua disciplina é {materia}")

nome_visitante = "kayky"
def disciplina():
    print(f"Seja bem-vindo a disciplina {disciplina}")

saudacao("Kayky")
disciplina("logica de programação")
#materia = "logica de programação"
#disciplina(materia)

saudacao(nome_visitante) # Chamando a função. 
disciplina(disciplina)