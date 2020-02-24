"""
Faça um programa que preencha um vetor com seis elementos numéricos inteiros. Calcule e mostre:
■ todos os números pares;
■ a quantidade de números pares;
■ todos os números ímpares;
■ a quantidade de números ímpares.

"""

# List
List = [1, 3, 2, 8, 66, 44, 11, 71, 12]
Pares, Impares = [], []
# Lista:
print(type(List))

Quantidade = len(List)
Inicio, Par, Impar = 0, 0, 0

for Inicio in range(0, Quantidade):
    if List[Inicio] % 2 == 0:
        Par += 1
        Pares.append(List[Inicio])
    else:
        Impar += 1
        Impares.append(List[Inicio])
print(f"par:{Par} que sao{Pares}, impar:{Impar} que sao {Impares}")
