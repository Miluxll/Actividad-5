#Diccionario de Precios de Productos
precios_prductos = {}
def productos(nombre, precio):
    precios_prductos [nombre] = precio
    print(f"Nombre: {nombre}")

def buscar(nombre):
    if nombre in precios_prductos:
        print(f"Nombre: {nombre}, prcio: {precios_prductos [nombre]}")
    else:
        print("Producto no encontrado")

while True:
    print("1. Agendar producto")
    print("2. Buscar producto")
    print("3. Salir")
    opcion = input("seleciona una opcion: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        precio = input("Precio: ")
        productos(nombre, precio)
        
    elif opcion == "2":
        nombre = input("Buscar producto: ")
        buscar(nombre)
        
    elif opcion == "3":
        break
    else:
        print("opion no valida")
