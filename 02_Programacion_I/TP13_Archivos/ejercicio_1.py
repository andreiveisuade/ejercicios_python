"""
Ejercicio 1:
Realizar un programa que permita actualizar una lista de precios en forma masiva. Deberá:\n1. Mediante una función generarOriginal, crear un archivo precios.csv con: Código (entero 4 dígitos); Precio (real); Descripción. Los campos se separan con ';'. Generar N productos de forma aleatoria.\n2. Desarrollar la función actualizarPrecios que recibe el nombre del archivo y un porcentaje de incremento, y crea un nuevo archivo Precios_actualizados.csv con los precios actualizados.\n3. Al finalizar, informar la cantidad de productos y el precio promedio con el incremento aplicado.
"""
import os
import random
