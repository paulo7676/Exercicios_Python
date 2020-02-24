"""
Fundamentos da Programação.Pascal, C C+ Java - Ascencio.pdf

2)Faça um programa que receba dois números, calcule e mostre a divisão do primeiro número pelo
segundo. Sabe-se que o segundo número não pode ser zero, portanto, não é necessário se preocupar com validações.

"""

PrimeiroNumero = int(input("Digite o Primeiro Numero"))
SegundoNumero = int(input("Digite o Segundo Numero"))

print(f"A divisao do numero {PrimeiroNumero} por {SegundoNumero} e igual a"
      f" {PrimeiroNumero/SegundoNumero} ou {PrimeiroNumero//SegundoNumero}")
