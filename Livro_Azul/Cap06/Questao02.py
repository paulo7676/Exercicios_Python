"""
Faça um programa que preencha um vetor com sete números inteiros, calcule e mostre:
■ os números múltiplos de 2;
■ os números múltiplos de 3;
■ os números múltiplos de 2 e de 3.
"""

Conjunto = [1, 3, 2, 6, 12, 7, 4, 2, 3, 66]
Dois, Tres, Ambos = [], [], []

# Metodo com menos funcoes
for i in range(0, len(Conjunto)):
    if Conjunto[i] % 3 == 0 and Conjunto[i] % 2 == 0:
        Ambos.append(Conjunto[i])
    elif Conjunto[i] % 3 == 0 and Conjunto[i] % 2 != 0:
        Tres.append((Conjunto[i]))
    elif Conjunto[i] % 3 != 0 and Conjunto[i] % 2 == 0:
        Dois.append((Conjunto[i]))
print(f"Os valores {Dois} sao multiplos de 2 ,Os valores {Tres} sao multiplos de 3 e, {Ambos} sao multiplos de ambos")

