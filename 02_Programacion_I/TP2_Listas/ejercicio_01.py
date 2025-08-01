"""
Ejercicio 1:
Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar su funcionamiento imprimiendo la lista luego de invocar a cada función:
a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de elementos también será un número al azar de dos dígitos. Realice la composición de la lista por comprensión y de la forma habitual (tendrá dos funciones distintas).
b. Calcular y devolver la sumatoria de todos los elementos de la lista anterior.
c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar se ingresa desde el teclado y la función lo recibe como parámetro. Utilice comprensión de listas para resolverlo.
d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas auxiliares. Un ejemplo de lista capicúa es [50,17,91,17,50].
"""

import random


def cargar_lista_aleatoria(cantidad_elementos): 
    """Cargar una lista con números al azar de cuatro dígitos."""
    return [random.randint(1000, 9999) for _ in range(cantidad_elementos)]


def calcular_sumatoria(lista):
    """Calcular y devolver la sumatoria de todos los elementos de la lista."""
    return sum(lista)


def eliminar_apariciones(lista, valor):
    """Eliminar todas las apariciones de un valor en la lista."""
    return [x for x in lista if x != valor]


def es_capicua(lista):
    """Determinar si el contenido de una lista cualquiera es capicúa."""
    return lista == lista[::-1]


def main():
    cantidad_elementos = random.randint(5, 10)  # Cantidad de elementos entre 10 y 99
    lista_aleatoria = cargar_lista_aleatoria(cantidad_elementos)

    
    sumatoria = calcular_sumatoria(lista_aleatoria)
    
    valor_a_eliminar = int(input("Ingrese un valor a eliminar de la lista: "))
    lista_filtrada = eliminar_apariciones(lista_aleatoria, valor_a_eliminar)
    
    
    def es_capicua(lista):
        return lista == lista[::-1]
    
    capicua_resultado = es_capicua(lista_filtrada)

if __name__ == "__main__":
    main()