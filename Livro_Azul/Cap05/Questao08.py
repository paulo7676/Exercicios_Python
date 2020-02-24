"""
 Faça um programa que receba a idade, o peso, a altura, a cor dos olhos (A — azul; P — preto; V — verde; e C — castanho)
 e a cor dos cabelos (P — preto; C — castanho; L — louro; e R — ruivo) de seis pessoas, e que calcule e mostre:
■ a quantidade de pessoas com idade superior a 50 anos e peso inferior a 60 kg;
■ a média das idades das pessoas com altura inferior a 1,50 m;
■ a porcentagem de pessoas com olhos azuis entre todas as pessoas analisadas; e
■ a quantidade de pessoas ruivas e que não possuem olhos azuis.

"""

Quantidade01, Quantidade02, Quantidade03, Quantidade04 = 0, 0, 0, 0
Idade02, OlhoAzul, Ruivas = 0, 0, 0

for pessoas in range(0, 3):
    Idade = int(input("Digite a sua Idade"))
    peso = float(input("digite o seu peso"))
    altura = float(input("digite a sua altura"))
    CorDosOlhos = input("Digite a cor dos seus olhos")
    CorDosCabelos = input("Digite a cor dos seus cabelos")
    if Idade > 50 and peso < 60:
        Quantidade01 += 1
    if altura <1.50:
        Quantidade02 +1
        Idade02 += Idade
    if CorDosOlhos == "A":
        OlhoAzul += 1
    elif CorDosOlhos != "A" and CorDosCabelos != "R":
        Ruivas +=1
print(f"A quantidade de pessoas com mais de 50 anos e {Quantidade01},"
      f" a media das alturas das pessoas com menos de 60 kg e {Idade02/Quantidade02}"
      f"porcentagem sla {(pessoas/OlhoAzul)*100}"
      f"Ruivos e é isso {Ruivas}")
