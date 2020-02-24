"""
Fundamentos da Programação.Pascal, C C+ Java - Ascencio.pdf

Faça um programa que receba dois números e execute uma das operações listads a seguir,de acrdo com a escolha do usuário.
Se for digitada uma opção inválida, mostre mensagem de erro e termine a execução do programa. As opções são:
a) O primeiro número elevado ao segundo número.
b) Raiz quadrada de cada um dos números.
c) Raiz cúbica de cada um dos números
"""

numero1 = int(input("Digite o primeiro numero"))
numero2 = int(input("Digite o segundo numero"))

print(f"a)o primeiro numero elevado ao segundo e {numero1 ** numero2}. "
      f"b)a raiz quadrada do primeiro numero e {numero1 ** 2} e do segundo numero e {numero2 ** 2}"
      f"c)a raiz cubica do primeiro numero e {numero1**3} e do segundo numero e {numero2 ** 3}")