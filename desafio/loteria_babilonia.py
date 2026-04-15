# Construa um progama que realiza o sorteio de um numero entre 1 e 15.
# O usuario tera 3 chances de acertar o valor.
# A cada tentativa voce deve informar se o chute e maior ou menor que o numero sorteado.
# Caso o usuario acerte, de os parabens.

#%%

import random

def get_input():
    while True:
        try:
            numero_usuario = int(input("Entre com um numero:"))

        except ValueError as err:
            print("valor invalido!")
            continue

        if 1 <= numero_usuario <= 15:
            return numero_usuario

        print("valor invalido! O numero deve ser entre 1 e 15")

def check_numbers(sorteio, usuario):

    if sorteio == usuario:
        print("parabens! vc acertou o numero")
        return True

    elif sorteio > usuario:
        print("numerio muito alto, Tente um numero mais baixo!")
        return False

    else:
        print("numero muito baixo, tente um numero mais alto!")
        return False

numero_sorteio = random.randint(1, 15)

for i in range(3):

    numero_usuario = get_input()
    
    if check_numbers(sorteio=numero_sorteio, usuario=numero_usuario):
        break

else:
    print("suas tentativas acabaram!")

# %%
