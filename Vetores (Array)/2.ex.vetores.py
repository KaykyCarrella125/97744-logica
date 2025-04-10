import os
os.system("cls || clear")

lista_notas = []

for i in range(10):
    nota = float(input("Digite uma nota: "))
    lista_notas.append(nota)

media = sum(lista_notas) / 10

print()
for nota in lista_notas:
    print(f"Nota: {nota:.1f}")

print()
print(f"Média: {media:.1f}")
print()
print(f"somente a primeira nota: {lista_notas[0]}")
print(f"somente a terceira nota: {lista_notas[2]}")
print(f"somente a quinta nota: {lista_notas[5]}")
print(f"somente a oitava nota: {lista_notas[7]}")