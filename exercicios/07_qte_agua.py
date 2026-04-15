# Faça um programa que vende uma garrafa de água:
# Se o cliente escolher água mineral natural, será cobrado R$1,50
# Se o cliente escolher água mineral com gás, será cobrado R$2,50

texto = """ 
Escolha sua agua para comprar:
(1) Agua mineral sem gas. - 1.50R$
(2) Agua mineral com gas. - 2.50R$
"""

opcao = input(texto)

valor_item = 0

if opcao == "1":
    valor_item = 1.50

elif opcao == "2":
    valor_item = 2.50

if valor_item == 0:
    print("nao temos nada assim por aqui!")

else:
    qtde = input("quantas garrafas gostaria?")
    qtde = int(qtde)

    valor_total = valor_item * qtde

    print ("sua conta deu: R$", valor_total)