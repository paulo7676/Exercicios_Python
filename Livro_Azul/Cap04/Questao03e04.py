"""
Fundamentos da Programação.Pascal, C C+ Java - Ascencio.pdf

3)Faça um programa que receba dois números e mostre o menor

4)Faça um programa que receba três números e mostre o maior

"""

# questao 03
""""
for num in range(0, 2):
    if num !=1:
        var1 = int(input("Digite o primeiro numero"))
    else:
        var2 = int(input("Digite o segundo numero"))
        if var1 >= var2:
            print(f"O numero {var1} e o maior")
        else:
            print(f"O numero {var2} e o maior")
"""

#questao 04(jeito inteligente de se fazer, fiz a 03 do jeito burro)

var = 0
for num in range(0, 3):
    numero = int(input("Digite um numero para saber se ele e o maior"))
    if numero >= var:
        var=numero
print(f"O numero {var} e o maior")

