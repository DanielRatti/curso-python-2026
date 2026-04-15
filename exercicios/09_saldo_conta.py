#Faça um programa que receba uma quantidade indefinida de valores correspondentes a “saldo em conta”
#mas quando o usuário apertar “enter” sem digitar valor algum, o programa para de receber valores
#exibe a soma de todos os valores digitados anteriormente.

saldo_total = 0

while True:
    saldo = input("entre com o saldo em conta: ")
    
    if saldo == "":
        break
    
    saldo_total += float(saldo)

print("total de saldo em contas:",saldo_total)