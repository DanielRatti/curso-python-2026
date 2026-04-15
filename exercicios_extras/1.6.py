#%%

segundos = input("digite os segundos para descobrir as horas, minutos e segundos:")
segundos = int(segundos)

horas = segundos // 3600

minutos = (segundos % 3600) // 60

segundos = segundos % 60

print(segundos, "convertido em 00:00:00 fica:", horas,"h:", minutos,"m:", segundos,"s")

# %%
