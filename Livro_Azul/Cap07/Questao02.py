"""
Crie um programa que preencha uma matriz 2  4 com números inteiros, calcule e mostre:
■ a quantidade de elementos entre 12 e 20 em cada linha;
■ a média dos elementos pares da matriz.
"""

from random import random

matriz = []
numerosPorLinha = []
media, Quantidade = 0, 0

for i in range(4):
    matriz.append([])
    for n in range(2):
        matriz[i].append([])
        matriz[i][n] = int(random()*30)

print(matriz)

for n in range(2):
    var = 0
    for i in range(4):
        if 12 < matriz[i][n] < 20:
            var += 1
        if matriz[i][n] % 2 == 0:
            media += matriz[i][n]
            Quantidade += 1
    print(f"Na linha {n} existem {var} com valores entre 12 e 20")
print(f"Existem tambem {Quantidade} numeros pares e sua media é {media/Quantidade}")

