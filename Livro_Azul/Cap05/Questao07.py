"""
Faça um programa que receba a idade, a altura e o peso de cinco pessoas, calcule e mostre:
■ a quantidade de pessoas com idade superior a 50 anos;
■ a média das alturas das pessoas com idade entre 10 e 20 anos;
■ a porcentagem de pessoas com peso inferior a 40 kg entre todas as pessoas analisadas.
"""

QuantidadeDePessoas50, MediaAltura10e20, PessoasParaMedia, PessoasParaPorcentagem=0, 0, 0, 0
PorcentagemInferior40 = 5

for pessoas in range(5):
    Peso = int(input("Digite o seu peso"))
    Idade = int(input("Digite a sua idade"))
    Altura = float(input("Digite a sua altura"))
    if Idade > 50:
        QuantidadeDePessoas50 += 1
    elif 10 <= Idade <= 20:
        MediaAltura10e20 += Altura
        PessoasParaMedia += 1
    if Peso < 40:
        PorcentagemInferior40 -= 1
print(f"Existem {QuantidadeDePessoas50} pessoas com mais de 50 anos,"
      f" {(MediaAltura10e20/PessoasParaMedia)} é a media do pesso de pessoas com idades entre 10 e 20 e,"
      f" a porcentagem de pessoas com peso inferior a 40kg e {100/PorcentagemInferior40}%")