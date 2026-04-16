# Faça o programa de uma sorveteria, onde o usuário pode escolher:
# Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
# Sabor do sorvete: morango, creme, chocolate
# Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)
# Apresente o valor a ser pago


#%%

tipo = input("escolha o tipo do sorvete entre casquinha / cascao / cestinha")
tipo = tipo.lower()

sabor = input("escolha o seu sabor de sorverte, entre morang / creme / chocolate")
sabor = sabor.lower()

cobertura = input("escolha a cobertura caramelo / morango / chocolate")
cobertura = cobertura.lower()

valor = 0

if tipo == "casquinha":
    valor += 1

elif tipo == "cascao":
    valor += 2.5

elif tipo == "cestinha":
    valor += 4

if cobertura in ["caramelo", "morango", "chocolate"]:
    valor += 1.5


txt = f"seu sorvete {tipo} de {sabor} com cobertura de {cobertura} custou R${valor:.2f}"

print(txt)
# %%
