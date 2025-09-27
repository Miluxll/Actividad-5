#Registro de Temperaturas Diarias
temperaturas_semana = []
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
print("Ingresa las temperaturas diarias de la semana:")
for dia in dias:
    while True:
        try:
            temp_str = input(f"Temperatura del {dia}: ")
            temperatura = float(temp_str) 
            temperaturas_semana.append((dia, temperatura)) 
            break 
        except ValueError:
            print("Entrada no válida.")
suma_temperaturas = 0
for tupla in temperaturas_semana:
    suma_temperaturas += tupla[1] 
temperatura_promedio = suma_temperaturas / len(temperaturas_semana)

print(f"\nLa temperatura promedio de la semana es: {temperatura_promedio:.2f}°C")
