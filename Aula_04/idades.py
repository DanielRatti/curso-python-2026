#%%
idades = []

while True:
    idade = input("entre com a idade:")

    if idade == "":
        break

    idades.append(int(idade))

print(idades)

media = sum(idades) / len(idades)
minima = min(idades)
maxima = max(idades)
qtde_idades = len(idades)

print("media:", media)
print("minima:", minima)
print("maxima:", maxima)
print("quantidade:", qtde_idades)
# %%
