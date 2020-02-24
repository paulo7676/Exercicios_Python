"""
Uma escola deseja saber se existem alunos cursando, simultaneamente, as disciplinas Lógica e Linguagem de Programação.
Coloque os números das mat rículas dos alunos que cursam Lógica e m um vetor , quinze alunos.
Coloque os números das matrículas dos alunos que cursam Linguagem de Programação em outro vetor, dez alunos.
Mostre o número das matrículas que aparecem nos dois vetores.
"""

Logica = [[1910400,"Rodrigo"], [1910401, "Paulo"], [1910402, "Mari"], [1910403, "Wendel"]]
Linguagem = [[1910404, "Arthur"], [1910401, "Paulo"], [1910400, "Rodrigo"]]


if len(Linguagem) >= len(Logica):
    for i in range(0, len(Logica)):
        for n in range(0, len(Linguagem)):
            if Logica[i][1] == Linguagem[n][1]:
                print(Logica[i])
else:
    for i in range(0, len(Linguagem)):
        for n in range(0, len(Logica)):
            if Linguagem[i][1] == Logica[n][1]:
                print(Linguagem[i])
