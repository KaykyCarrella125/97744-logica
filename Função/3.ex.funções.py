import os 

os.system("cls || clear")

def saudacao(nome, nome_disciplina):
    print(f"Olá {nome}! Bem-vindo(a) ao curso de DS!")
    print(f"A disciplina {nome_disciplina} faz parte de curso de DS.")


nome = input("Digite seu nome: ")
nome_disciplina = input("Digite sua disciplina: ")
