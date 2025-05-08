import os
os.system("cls || clear")

from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int

Pessoa1 = Pessoa("Kayky", 20)
Pessoa2 = Pessoa("Samira", 19)

print(f"\nNome: {Pessoa1.nome} tem {Pessoa1.idade} anos")
print(f"\nNome: {Pessoa2.nome} tem {Pessoa2.idade} anos")