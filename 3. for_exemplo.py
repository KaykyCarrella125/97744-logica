import os

os.system("cls || clear")

#exemplo de uso de repetição while.
while True:
    idade = int(input("digite a sua idade: "))

    if idade < 18:
        print("Não autorizado. \nSomente maiores de 18.\n")
    else:
        break

print("acesso permitido. ")
print("Fim.")