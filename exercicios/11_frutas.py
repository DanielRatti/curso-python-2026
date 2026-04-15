#%%

fruta = input("entre com o nome da fruta:")

Frutas = {
    "Pera": "R$1,25",
    "Goiaba": "R2,25",
    "Abacaxi": "R$3,25",
    "Jaca": "R$5,25",
    "Laranja": "R$0,25",
    "Limao": "R$3,25",
    "Maca": "R$4,25",
    "Banana": "R$3,35",
    "Uva": "R$5,45",

}

if fruta in Frutas:
    print(Frutas[fruta])

else:
    print("Insira uma fruta valida!")
