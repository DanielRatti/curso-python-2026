#%%

from this import d


lista = [2, 132, "daniel", ["ds", "de", "da"], True ]

lista[2]


#%%

# pares de chaves/valor

dados_daniel = {
        "nome":"daniel",
        "sobrenome":"pinheiro", 
        "filhos":False,
        "formacao":["administracao", "progamacao fullstack"],
        "cargos":[
            {"nome":"ds jr", "empresa": "empresa1"},
            {"nome":"ds pl", "empresa": "empresa2"},
            {"nome":"ds sr", "empresa": "empresa3"},
            {"nome":"ds spec", "empresa": "empresa4"},
        ]
        
}

print(dados_daniel)

#%%

print(dados_daniel["formacao"][-1])
print(dados_daniel["cargos"][-1]["empresa"])
print(dados_daniel["cargos"][-1]["nome"])


#%%
dados_daniel["estado civil"] = "casado"

print(dados_daniel)

#%%

print("chaves:", dados_daniel.keys())

print("valores:",dados_daniel.values())

print("items:", dados_daniel.items())


#%%

for i in [10, 20, 45, 28, "daniel"]:
    print(i)


#%%

for i in dados_daniel:
    print(i, "->", dados_daniel[i])


#%%

for item in dados_daniel.items():
    print(item)

#%%

for chave, valor in dados_daniel.items():
    print(chave, "->", valor)


#%%
