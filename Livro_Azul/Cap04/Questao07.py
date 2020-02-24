"""
Fundamentos da Programação.Pascal, C C+ Java - Ascencio.pdf

Uma empresa decide dar um aumento de 30% aos funcionários com salários inferiores a R$ 500,00.
Faça um programa que receba o salário do funcionário e mostre o valor do salário reajusta do ou uma mensagem,
caso ele não tenha direito ao aumento.
"""

Sal = float(input("Digite o salario do seu funcionario"))
if Sal <= 500:
    Sal *= 1.3
    print(f"O seu salario apos o ajuste e {Sal}")
else:
    print("Voce nao tem direito ao salario")
