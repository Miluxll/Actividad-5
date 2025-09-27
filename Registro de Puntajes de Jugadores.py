#Registro de Puntajes de Jugadores
puntaje_jugadores = {}
def puntajes(nombre, putaje):
    puntaje_jugadores [nombre] = puntaje
    print(f"Nombre: {nombre}")

def mostrar_jugador():
    if puntaje_jugadores:
        print("Jugadores: ")
        for nombre, puntaje in puntaje_jugadores.items():
             print(f"Nombre: {nombre}, puntaje: {puntaje}")
    else:
        print("No se encuentran jugadores.")

while True:
    print("1. Agendar jugador")
    print("2. Mostrar jugador")
    print("3. Salir")
    opcion = input("seleciona una opcion: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        puntaje = input("puntaje: ")
        puntajes(nombre, puntaje)
        
    elif opcion == "2":
        mostrar_jugador()
        
    elif opcion == "3":
        break
    else:
        print("opion no valida")
