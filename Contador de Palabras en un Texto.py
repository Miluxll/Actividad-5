#Contador de Palabras en un Texto
texto = input("")
palabras = texto.split(" ")
contador = {}
for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1
for palabra in contador:
    frecuencia = contador[palabra]
    print(f"{palabra} su frecuencia es de: {frecuencia}")
