#Ordenamiento de Puntos en el Plano
import math
def ordenar_puntos_por_distancia(puntos):
  return sorted(puntos, key=lambda punto: math.sqrt(punto[0]**2 + punto[1]**2))
lista_de_puntos = [(3, 5), (4, 2), (5, 0), (-1, 1), (0, 0),]
puntos_ordenados = ordenar_puntos_por_distancia(lista_de_puntos)
print(f"Puntos ordenados por distancia al origen: {puntos_ordenados}")
