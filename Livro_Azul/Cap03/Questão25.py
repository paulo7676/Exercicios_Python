"""
Fundamentos da Programação.Pascal, C C+ Java - Ascencio.pdf

25)Faça um programa que receba uma hora (uma variável para hora e outra para minutos), calcule e mostre:
a) a hora digitada convertida em minutos;
b) o total dos minutos, ou seja, os minutos digitados mais a conversão anterior;
c) o total dos minutos convertidos em segundos

"""

Hora = int(input("Digite a Hora"))
Minutos = int(input("Digite os minutos"))
print(f"A Hora {Hora} convertida em minutos e {Hora*60}, o total de minutos e {(Hora*60)+Minutos} "
      f"E o total de segundos é {(Hora*360)+(Minutos*60)}")
