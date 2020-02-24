"""
Faça um programa para controlar o estoque de mercadorias de uma empresa. Inicialmente, o programa deverá preencher dois
vetores com dez posições cada, onde o primeiro corresponde ao código do produto e o segundo,
ao total desse produto em estoque. Logo após, o programa deverá ler um conjunto indeterminado de dados contendo
o código de um cliente e o código do produto que ele deseja comprar, juntamente com a quantidade.
Código do cliente igual a zero indica fim do programa. O programa deverá verificar:

-Fiz Um Dicionario

■ se o código do produto solicitado existe. Se existir, tentar atender ao pedido;
caso contrário, exibir mensagem Código inexistente;

■ cada pedido feito por um cliente só pode ser atendido integralmente.
Caso isso não seja possível, escrever a mensagem Não temos estoque suficiente dessa mercadoria.
Se puder atendê-lo, escrever a mensagem Pedido atendido. Obrigado e volte sempre

■ efetuar a atualização do estoque somente se o pedido for atendido integralmente;

■ no final do programa, escrever os códigos dos produtos com seus respectivos e stoques já atualizados.

"""
codigo = "True"
Dicionario = {"Playstation": 5, "Xbox": 3, "Nintendo": 2, "Computador": 5, "Gameboy": 1}
ExisteProduto = False
Produto = " "

while codigo == "True":
    Produto = input("Digite o valor do produto para ver se temos no estoque")
    # Ver se a chave existe
    if Produto in Dicionario:
        print(f"Existe o produto {Produto} na lista")
        Quantidade = int(input("Digite a Quantidade de objetos que deseja comprar"))
        if Quantidade <= Dicionario[Produto]:
            Quantidade = Dicionario[Produto] - Quantidade
            Dicionario[Produto] = Quantidade
        else:
            print("Nao foi possivel atender devido a falta de Estoque")
    else:
        print("nao temos esse valor no estoque")
    codigo = input("Ainda deseja continuar a compra?")

print(Dicionario)
