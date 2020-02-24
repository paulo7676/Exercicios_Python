"""
Faça um programa que preencha um vetor com os nomes de sete alunos e carregue outro vetor com a média final dessesalunos
Calcule e mostre:
■ o nome do aluno com maior média (desconsiderar empates);

■ para cada aluno não aprovado, isto é, com média menor que 7, mostrar quanto esse aluno precisa tirar na prova
de exame final para ser aprovado.

Considerar que a média para aprovação no exame é 5.


"""

notas = [10, 7, 9, 4, 10, 7, 11]
Alunos = ["aluno1", "aluno2", "aluno3", "aluno4", "aluno5", "aluno6", "aluno7"]
AlunosRuins = []
for i in range(0, 7):
    if i == 0:
        Maior = [Alunos[i], notas[i]]
    elif Maior[1] < notas[i]:
        Maior = [Alunos[i], notas[i]]
    if notas[i] < 7:
        NotaNecessaria = 2 * (5 - (notas[i] / 2))
        AlunosRuins = [Alunos[i], NotaNecessaria]
print(f"Alunos 'Reprovados':\n{AlunosRuins}\n, e o melhor aluno foi {Maior} ")
