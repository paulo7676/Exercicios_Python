"""
 Faça um programa que receba a idade de oito pessoas, calcule e mostre: a) a quantidade de pessoas em cada faixa etária;
 b) a porcentagem de pessoas na primeira faixa etária com relação ao total de pessoas.
c) a porcentagem de pessoas na última faixa etária com relação ao total de pessoas

1a Até 15 anos
2a De 16 a 30 anos
3a De 31 a 45 anos
4a De 46 a 60 anos
5a Acima de 60 anos

"""
Ate15, Entre16e30, Entre31e45, Entre46e60, AcimaDe60 = 0, 0, 0, 0, 0

for pessoas in range(8):
    idade = int(input("Digite a sua idade em anos"))
    if idade <= 15:
        Ate15 += 1
    elif 15 < idade <= 30:
        Entre16e30 += 1
    elif 30 < idade <= 45:
        Entre31e45 += 1
    elif 45 < idade <= 60:
        Entre46e60 += 1
    elif idade > 60:
        AcimaDe60 += 1
print(f"Existem {Ate15} pessoas com menos de 15 anos, "
      f"{Entre16e30} entre 16 e 30, {Entre31e45} entre 31 e 45 , "
      f"{Entre46e60} entre 46 e 60 e, {AcimaDe60} acima de 60 ")
