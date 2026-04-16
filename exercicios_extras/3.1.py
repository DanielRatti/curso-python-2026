# Faca um progama que conte quantas vezes a letra "a" aparece em uma palavra

#%%

palavra = input("digite uma palavra: ")

count = 0

for letra in palavra:
    count += letra == "a"
        
print(f"a palavra {palavra} repete {count} vezes a letra a.")


# %%
