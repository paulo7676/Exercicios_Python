"""
Fundamentos da Programação.Pascal, C C+ Java - Ascencio.pdf

05)Faça um programa que receba dois números e execute as operações listadas a seguir,de acordo com a escolha do usuário.
1 Média entre os números digitados
2 Diferença do maior pelo menor
3 Produto entre os números digitados
4 Divisão do primeiro pelo segundo

Se a opção digitada for inválida, mostre uma mensagem de erro e termine a execução do programa.
Lembre-se de que, na operação 4, o segundo número deve ser diferente de zero.
"""

numero1 = int(input("Digite o primeiro numero"))
numero2 = int(input("Digite o segundo numero"))
operacao = int(input("1 Média entre os números digitados,2 Diferença do maior pelo menor,"
                     "3 Produto entre os números digitados,4 Divisão do primeiro pelo segundo"))
if 0 > operacao > 5:
    print(f"recebermos o numero {operacao}")
elif operacao == 1:
    print(f"Media dos numeros :{(numero1+numero2)/2}")
elif operacao == 2:
    if numero2 > numero1:
        _ = numero1
        numero1 = numero2
        numero2 = _
    print(f"Diferenca do maior para o menor e {numero1-numero2}")
elif operacao == 3:
    print(f"O produto dos numero e {numero1*numero2}")
elif operacao == 4:
    print(f"A divisao dos numeros e {numero1/numero2}")


