#%%

#Uma maneira de definir listas

from typing import TextIO


idades = [28, 42, 35, 39, 28, 38]

print(idades)

#%%

daniel = [ "daniel", "giovanna", 27, 1, "namorando", 2342.98]

print(daniel) 

# %%

type(daniel)

# %%
print(daniel[2])

print (daniel[5])

print (daniel[0])


#%%

idades = [28, 42, 35, 39, 28, 38, 42]

print("soma idades:", sum(idades))

print ("qtde idades:", sum(idades) / len(idades))

print("menor idade:", min(idades))

print ("maior idade:", max(idades))


#%%

daniel = [ "daniel",
        27,
        False, 
        "namorando", 
        ["prefeitura", "secretario", "insight", "teste1", "teste2"],
        ["estagiario", "auxiliar adm", "head de dados"],
        [340, 600, 1900, 17000]
        ]

print(len(daniel))

print(daniel[4][0])

jobs = daniel[4]
primeiro_job = jobs[0]
print("meu primeiro trabalho foi:", primeiro_job)

#%%

tamanho = len(daniel)
pos = tamanho - 1

salario = daniel[pos]

daniel[pos][len(salario) -1]

#%%
#PRIMEIROS 4 ELEMENTOS
daniel[0:4]


#%%

daniel[4][3:5]

#%%

print(daniel[4][3:])
print(daniel[4][-2:])

# %%

#PRIMEIROS 4 ELEMENTOS
daniel[:4]

# %%

salarios = daniel[6]
salarios[::2]