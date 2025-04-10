import os
os.system("cls || clear")

nota1 = float(input("Digite uma nota: "))
nota2 = float(input("Digite uma nota: "))
nota3 = float(input("Digite uma nota: "))

soma = nota1 + nota2 + nota3
media = soma / 3

print(f"Média: {media:.1f}")