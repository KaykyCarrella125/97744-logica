import os
import time
os.system("cls || clear")



while True:
    print("= Gerenciador de nome =")
    print("1 - Adicionar")
    print("1 - Listar nomes")
    print("3 - Atalizar")
    print("4 - Excluir")

    opcao = int(input("Digite uma das opções acima: "))

    match opcao:
        case 1:
            adicionar(nomes)
        case 2:
            mostrar(nomes)
        case 3:
            atualizar(nomes)
        case 4:
            excluir(nomes)
        case 5:
            print("\nSaindo do programa.")
            break
    if opcao != 1:
        time.sleep(5)
    os.system("cls || clear")
