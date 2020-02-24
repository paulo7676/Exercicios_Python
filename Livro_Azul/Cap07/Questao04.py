"""
Faça um programa que receba: ■ as notas de 15 alunos em cinco provas diferentes e armazene-as em uma matriz 15  5;
■ os nomes dos 15 alunos e armazene-os em um vetor de 15 posições. O programa deverá calcular e mostrar:
■ para cada aluno, o nome, a média aritmética das cinco provas e a situação (aprovado, reprovado ou exame);
■ a média da classe.


Vale resaltar que pra poupar tempo vou fazer uma matriz 5 x 3
"""

MatrizNotas = []
Alunos = ["Wendel", "paulo", "Mari", "Hualison", "Pedro"]

for i in range(5):
    MatrizNotas.append([])
    for n in range(3):
        MatrizNotas[i].append(int(input(f"Digite a {n+1}º nota do aluno {Alunos[i]}")))

for i in range(5):
    media = 0
    for n in range(3):
        media += MatrizNotas[i][n]
    if (media/3) <= 5:
        situacao = "Reprovado"
    else:
        situacao = "Aprovado"
    print(f"O aluno {Alunos[i]} tem media {media/3} e esta {situacao}")
