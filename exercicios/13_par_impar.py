#%%

def par_impar(numero:int):
    if numero % 2 == 0:
        print(numero, "e par!!!")
    else:
        print(numero, "e impar!!!")


numero = input("entre com um numero:")
numero = int(numero)

par_impar(numero)
# %%
