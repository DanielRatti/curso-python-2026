# Faça um programa que vende uma garrafa de água:
# Se o cliente escolher água mineral natural, será cobrado R$1,50
# Se o cliente escolher água mineral com gás, será cobrado R$2,50

texto = """ 
Escolha sua agua para comprar:
(1) Agua mineral sem gas.
(2) Agua mineral com gas.
"""

opcao = input(texto)

conta = 0

if opcao == "1":
    conta = 1.50

elif opcao == "2":
    conta = 2.50

if conta == 0:
    print("nao temos nada assim por aqui!")

else:
    print("sua conta deu:", conta,"R$")