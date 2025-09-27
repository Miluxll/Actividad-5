#Agenda de Contactos
agenda_telefonica = {}
def agenda_contacto(nombre, telefono):
    agenda_telefonica[nombre] = telefono
    print(f"Nombre: {nombre}")
    
def buscar_contacto(nombre):
    if nombre in agenda_telefonica:
        print(f"Nombre: {nombre}, telefono: {agenda_telefonica[nombre]}")
    else:
        print(f"No se encontro contacto")

def eliminar_contacto(nombre):
    if nombre in agenda_telefonica:
        del agenda_telefonica[nombre]
        print(f"Contacto eliminado")
    else:
        print("Contacto no encontrado")
        
while True:
    print("1. Agendar contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Salir")
    opcion = input("seleciona una opcion: ")
    
    if opcion == "1":
        nombre = input("Nombre: ")
        telefono = input("Telefono: ")
        agenda_contacto(nombre, telefono)
        
    elif opcion == "2":
        nombre = input("Buscar contactos: ")
        buscar_contacto(nombre)
        
    elif opcion == "3":
         nombre = input("Eliminar contacto: ")
         eliminar_contacto(nombre)
         
    elif opcion == "4":
        break
    else:
        print("opion no valida")
