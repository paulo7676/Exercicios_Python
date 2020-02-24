"""
Faça um programa que receba o total das vendas de cada vendedor de uma loja e armazene-as em um vetor.
Receba também o percentual de comissão a que cada vendedor tem direito e armazene-os em outro vetor.
Receba os nomes desses vendedores e armazene-os em um terceiro vetor. Existem apenas dez vendedores na loja.
Calcule e mostre:
■ um relatório com os nomes dos vendedores e os valores a receber referentes à comissão;
■ o total das vendas de todos os vendedores;
■ o maior valor a receber e o nome de quem o receberá;
■ o menor valor a receber e o nome de quem o receberá.

"""

Lista = [["Jefferson", 0.15], ["Paulo", 0.25], ["Ronaldo", 0.10], ["Alexandro", 0.05], ["Joana", 0.20]]
total, Maior, Menor = 0, 0, 0

for i in range(0, len(Lista)):
    valor = int(input(f"Digite o valor que o vendedor {Lista[i][0]} apurou na semana"))
    total += valor
    Lista[i].append(valor)

    if i == 0:
        Maior = [[Lista[i][0], valor * Lista[i][1]]]
        Menor = [[Lista[i][0], valor * Lista[i][1]]]

    elif Maior[0][1] < (valor * Lista[i][1]):
        Maior = [[Lista[i][0], valor * Lista[i][1]]]

    elif (valor * Lista[i][1]) > Menor[0][1]:
        Menor = [[Lista[i][0], valor * Lista[i][1]]]
        

print(f"Relatorio:\n {Lista} \n, total de vendas :{total}, maior valor foi o de {Maior[0][0]} com o valor {Maior[0][1]}"
      f", menor valor foi o de {Menor[0][0]} com o valor {Menor[0][1]}")
