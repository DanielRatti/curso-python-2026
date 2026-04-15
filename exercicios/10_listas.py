# Escreva um programa que receba uma lista de numeros
# do usuario e conte quantas vezes um numero
# especifico aparece na lista
# solicite ao usuario um numero e exiba a contagem.
#%%
lista = [1,2,3,3,2,1,1,1,1,5,6,7,7,6,5]

numero = input("entre com um numero:")
numero = int(numero)


contador = 0
for i in lista:
    if i == numero:
        contador +=1

print("quantidoade de", numero, ":", contador)
