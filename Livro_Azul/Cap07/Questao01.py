"""
Faça um programa que preencha uma matriz 3  5 com números inteiros,
calcule e mostre a quantidade de elementos entre 15 e 20.
"""

from random import random

matriz = []
valores = 0

for i in range(3):
    matriz.append(list())
    for n in range(5):
        matriz[i].append(int(random()*30))
        if 15 < matriz[i][n] < 20:
            valores += 1

print(f"A matriz é {matriz} \n e possuimos {valores} valores entre 15 e 20 ")
