"""
Fundamentos da Programação.Pascal, C C+ Java - Ascencio.pdf

Faça um programa que receba:
-o código do produto comprado;
-a quantidade comprada do produto. Calcule e mostre:

o preço unitário do produto comprado, seguindo a Tabela I;  o preço total da nota;

o valr do desconto,seguindo a Tabela II e aplicdo sobre o preço total da nota;e o prço final da nota depois do desconto.

TABELA I:
O 1 a 10 R$ 10,00 . 11 a 20 R$ 15,00 . 21 a 30 R$ 20,00 . 31 a 40 R$ 30,00

TABELA II:
O Até R$ 250,00 5% . Entre R$ 250,00 e R$ 500,00 10% . Acima de R$ 500,00 15%

"""

quantidade = int(input("Digite a quantidade de objetos"))

if 1 < quantidade < 11:
    valor = quantidade*10
elif 11 < quantidade < 21:
    valor = quantidade*15
elif 21 < quantidade < 31:
    valor = quantidade*20
elif 31 < quantidade < 41:
    valor = quantidade*30

if valor == 250:
    print(f"valor e {valor} e com o desconto ele fica {valor*0.95}")
elif 250 < valor < 500:
    print(f"valor e {valor} e com o desconto ele fica {valor*0.90}")
elif valor > 500:
    print(f"valor e {valor} e com o desconto ele fica {valor * 0.85}")

