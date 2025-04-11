import os
os.system("cls || clear")

lista_de_compras = []
QUANTIDADE = 3

print("= LISTA DE COMPRAS =")
for i in range(QUANTIDADE):
    item = input("Digite um item para lista: ")
    lista_de_compras.append(item)

print("\n= ITENS DA LISTA =")
for item in lista_de_compras:
    print(item)