#Diccionario de Traducción de Palabras
traductor = {}
palabras = input("Escribe: ")
for i in palabras.split(","):
    clave, valor = i.split(":")
    traductor[clave] = valor
frase = input("Escribe para traducir: ")
for j in frase.split(" "):
    if j in traductor:
        print(traductor[j], end = " ")
    
