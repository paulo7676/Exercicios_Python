"""
Fundamentos da Programação.Pascal, C C+ Java - Ascencio.pdf

Faça um programa que receba quatro notas de um aluno,
calcule e mostre a média aritmética das notas e a mensagem de aprovado ou reprovado, considerando para aprovação média 7.
"""

notaFinal = 0
for num in range(4):
    nota = int(input(f"Digite a sua {num + 1}° nota"))
    notaFinal += nota
    if num == 3:
        if (notaFinal / 4) >= 7:
            print(f"aprovado ,nota final {notaFinal / 4}")
        else:
            print(f"reprovado, nota final {notaFinal / 4}")
