#Cargar los datos desde el archivo productos.csv

import pandas as pd

datos = pd.read_csv("C:/Users/yinat/OneDrive/Documents/Segundo Parcial Python/productos.csv")
print(datos)

#Calcular el precio promedio de los productos.

promedio = datos['precio'].mean()
print('')
print('@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@')
print('')
print(" El promedio de los precios es:", promedio)

#Manejar excepciones al leer archivos.
try:

    #He probado cambiando el nombre de la ubicacion con una que no existe para verificar que si funciona
    archivo = open("C:/Users/yinat/OneDrive/Documents/Segundo Parcial Python/productos.csv", "r")
    contenido = archivo.read()

except FileNotFoundError:
    print("Error: El archivo no se encontró.")

except PermissionError:
    print("Error: No tienes permisos para acceder al archivo.")

except Exception as e:
    print("Error:", e)

finally:
    archivo.close()

#Utilizar funciones lambda para aplicar descuentos.

datos["descuento"] = datos["precio"] * (datos["porcentaje_descuento"] / 100)
datos["precio_final"] = datos["precio"] - datos["descuento"]
print('')
print('@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@')
print('')
print(datos)
print('')
print('GRACIAS POR LA COMPRA!')
