#Registro de Ventas por Producto y Mes
cantidad_vendida = {}
def venta(producto, mes):
    cantidad_vendida[producto] = mes
    print(f"Producto: {producto}")
    
def mostrar_ventas():
    if cantidad_vendida:
        print("ventas del mes: ")
        for nombre, puntaje in cantidad_vendida.items():
             print(f"Nombre: {producto}, Venta: {mes}")
        
while True:
    print("1. Agendar producto")
    print("2. mostrar ventas")
    print("3. Salir")
    opcion = input("seleciona una opcion: ")
    
    if opcion == "1":
        producto = input("Nombre: ")
        mes = input("ventas: ")
        venta(producto, mes)
        
    elif opcion == "2":
        mostrar_ventas()
        
    elif opcion == "3":
        break
    else:
        print("opion no valida")
