# Faca um progama que verifique se a pessoa pertence a familia "calvo" ou "silva"

#%%

nome = input("entre com seu nome e sobrenome: ")
nome_split = nome.lower().split(" ")

if "calvo" in nome_split:
    print("Essa pessoa e calvo!!")
 
if "silva" in nome_split:
    print("essa pessoa e silva!!!")\

if "silva"  not in nome_split and "calvo" not in nome_split:
    print("Essa pessoa nao e silva nem calvo")

