import os 
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Pessoa:
    nome: str
    idade: int

@dataclass
class Pet:
    nome: str
    idade: int
    peso: float

Pessoa1 = Pessoa("Kayky", 20)
Pessoa2 = Pessoa("Samira", 19)

pet1 = Pet("Mia", 4, 7.8)
pet2 = Pet("Lisa", 3, 4.7)

print("\n' Dados da pessoa =")
print(f"Nome: {Pessoa1.nome} tem {Pessoa1.idade} anos")
print(f"Nome: {Pessoa2.nome} tem {Pessoa2.idade} anos")

print("\n= Dados da pessoa =")
print(f"Nome: {pet1.nome}, idade: {pet1.idade}, peso: {pet1.peso}")
print(f"Nome: {pet2.nome}, idade: {pet2.idade}, peso: {pet2.peso}")