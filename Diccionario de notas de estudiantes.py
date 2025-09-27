#Diccionario de Notas de Estudiantes
def registrar_notas():
    estudiantes = {}
    
    while True:
        nombre = input("Ingresa el nombre del estudiante : ")
        if nombre.lower() == "fin":
            break 

        calificaciones = [] 
        while True:
            try:
                nota_str = input(f"Ingresa una calificación ")
                if nota_str.lower() == 4:
                    break 

                nota = float(nota_str)  
                calificaciones.append(nota)
            except ValueError:
                print("Entrada no válida.")

        estudiantes[nombre] = calificaciones  

    return estudiantes

def mostrar_estudiantes(estudiantes):
 
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return

    print("Lista de Estudiantes ")
    for nombre, calificaciones in estudiantes.items():
        print(f"Estudiante: {nombre}")
        if calificaciones:
            print(f"  Calificaciones: {', '.join(map(str, calificaciones))}")
        else:
            print("  No tiene calificaciones registradas.")

if __name__ == "__main__":
    datos_estudiantes = registrar_notas()
    mostrar_estudiantes(datos_estudiantes)

