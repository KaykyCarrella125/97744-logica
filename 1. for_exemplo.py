import os

os.system("cls || clear")

#exemplo de uso de repetição while.
idade = int(input("digite a sua idade: "))

while idade < 18:
    print("Não autorizado. \nSomente maiores de 18.\n")
    idade = int(input("digite sua idade: "))

print("acesso permitido. ")
print("Fim.")