"""
 Uma loja utiliza o código V para transação à vista e P para transação a prazo.
Faça um programa que receba o código e o valor de quinze transações, calcule e mostre:
■ o valor total das compras à vista;
■ o valor total das compras a prazo;
■ o valor total das compras efetuadas; e
■ o valor da primeira prestação das compras a prazo juntas, sabendo-se que serão pagas em três vezes.
"""

ValorVista, ValorPrazo, ValorPrazo1 ,ValorTotal = 0, 0, 0, 0
for compras in range(0, 3):
    TipoDeCompra = input("Digite o tipo de compra (V para a vista , P para prazo)")
    ValorDaCompra = float(input("Digite o valor da compra"))
    ValorTotal += ValorDaCompra
    if TipoDeCompra == "V":
        ValorVista += ValorDaCompra
    else:
        ValorPrazo += ValorDaCompra
        ValorPrazo1 += (ValorDaCompra/3)
print(f"O valor das compras ao todo e {ValorTotal}, divididas em {ValorVista} a Vista , {ValorPrazo} a Prazo e ,"
      f" {ValorPrazo1} na primeira parcela a Prazo")
