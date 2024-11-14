# Proyecto: Compra Fruteria
# Estudiante: Jose Pablo Delgado
# Fecha de Inicio: 13/11/2024
# Fecha de Entrega: 13/11/2024
# Descripción: Comtrolar compras de frutas y verduras
# Version 0.0
from analisis_datos import *

#Generar una lista de compras aleatoria y escribir esta lista en un archivo
lista_compras = generar_lista_compras()
guardar_lista_compras(lista_compras)
precios = [precio for _, precio in lista_compras]
media = media(precios)
mediana = mediana(precios)
print(f"Media de precios: ¢{media:.2f}")
print(f"Mediana de precios: ¢{mediana:.2f}")
