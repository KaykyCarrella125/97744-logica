import os 

os.system("cls || clear")

idade = int(input("digite sua idade: "))

while idade < 10:
    print("Não autorizado. \nSomente para maiores de 10.\n")
    idade = int(input("digite sua idade: "))

print("acesso permitido. ")
print("Bem-vindo seu gostoso.")