"""
04)Faça um programa que preencha um vetor com quinze elementos inteiros e verifique
a existência de elementos iguais a 30, mostrando as posições em que apareceram.
"""

from random import random

lista = []

for i in range(0, 15):
    lista.append(int(random()*40))
    if lista[i] == 30:
        print(f"O numero 30 esta na posicao {i}")
print(lista)

if 30 in lista:
    print("Existe um 30 na lista")
