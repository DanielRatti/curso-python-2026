#%%

def calc_imposto(preco:float, tx_imposto_base:float, **kwargs):
    imposto = preco * tx_imposto_base

    for i in kwargs:
        print(i, kwargs[i])
        imposto += preco * kwargs[i]

    return imposto


# %%

impostos_gerais = {
    "municipio": 0.05,
    "estadual": 0.005,
    "nacional": 0.001
}

calc_imposto(100, 0.3, **impostos_gerais, internacional=0.00001)

# %%
