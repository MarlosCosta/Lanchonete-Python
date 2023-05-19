#Exercicio 2 de 4 do Trabalho
#Cardapio e identificador pessoal
print("Bem Vindo a Lanchonete do Marlos Augusto da Costa")
print("*******************Cardápio*********************")
print("| Código |        Descrição           | Valor |")
print("|   100  |     Cachorro Quente        |  9,00 |")
print("|   101  |   Cachorro Quente Duplo    | 11,00 |")
print("|   102  |          X-Egg             | 12,00 |")
print("|   103  |         X-Salada           | 12,00 |")
print("|   104  |          X-Bacon           | 14,00 |")
print("|   105  |          X-Tudo            | 17,00 |")
print("|   200  |    Refrigerante Lata       |  5,00 |")
print("|   201  |        Chá Gelado          |  4,00 |")

#Declaração da variavel acumuladora que vai guardar o valor dos produtos pedidos
totalPedido = 0
while True:
    codigoProduto = input("Digite o código desejado: ")
    if codigoProduto != "100" and codigoProduto != "101" and codigoProduto != "102" and codigoProduto != "103" \
            and codigoProduto != "104" and codigoProduto != "105" and codigoProduto != "200" and codigoProduto != "201":
        print("Código Inválido!")
        continue #Caso usuário digite um código fora do cardapio, volta para o começo do While

    if codigoProduto == "100":
        print("Você pediu um Cachorro Quente no valor de R$9,00")
        totalPedido = totalPedido + 9.00
    if codigoProduto == "101":
        print("Você pediu um Cachorro Quente Duplo no valor de R$11,00")
        totalPedido = totalPedido + 11.00
    if codigoProduto == "102":
        print("Você pediu um X-Egg no valor de R$12,00")
        totalPedido = totalPedido + 12.00
    if codigoProduto == "103":
        print("Você pediu um X-Salada no valor de R$12,00")
        totalPedido = totalPedido + 12.00
    if codigoProduto == "104":
        print("Você pediu um X-Bacon no valor de R$14,00")
        totalPedido = totalPedido + 14.00
    if codigoProduto == "105":
        print("Você pediu um X-Tudo no valor de R$17,00")
        totalPedido = totalPedido + 17.00
    if codigoProduto == "200":
        print("Você pediu um Refrigerante Lata no valor de R$5,00")
        totalPedido = totalPedido + 5.00
    if codigoProduto == "201":
        print("Você pediu um Chá Gelado no valor de R$4,00")
        totalPedido = totalPedido + 4.00

    #Pergunta se o usuario quer pedir mais alguma coisa
    continuarPedido = input("Deseja pedir mais alguma coisa (S pra SIM / Outra tecla para FINALIZAR)? ")
    continuarPedido = continuarPedido.upper() #permite o usuário digitar letra maiuscula ou minuscula
    if continuarPedido == "S": #Respondendo S, volta para o inicio do While
        continue
    else: #Respondendo qualquer coisa diferente de S, o pedido será finalizar apresentando o total a pagar
        print("O total a ser pago é: R${:.2f}" .format(totalPedido))
        break



