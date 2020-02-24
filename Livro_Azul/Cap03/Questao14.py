"""
Fundamentos da Programação.Pascal, C C+ Java - Ascencio.pdf

14)Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:
a) a idade dessa pessoa em anos;
b) a idade dessa pessoa em meses;
c) a idade dessa pessoa em dias;
d) a idade dessa pessoa em semanas.

"""

AnoAtual = int(input("Digite o Ano em que estamos"))
AnoNascimento = int(input("Digite o Ano do Seu Nascimento"))
Idade = AnoAtual-AnoNascimento
print(f"A sua idade em anos e {Idade} ,em meses {Idade*12} , em dias {Idade*12*30} ,em semanas {Idade*12*4}")
