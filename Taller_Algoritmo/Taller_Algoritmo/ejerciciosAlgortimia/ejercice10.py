"""

Con la lista del ejercicio 6, diseñar una solución que calcule la media de todos los números

-------------------------------------
PROG lista_random
    lista = GENERAR 20 numeros aleatorios entre 1 Y 100
    suma = 0
    contador = 0
    PARA i DESDE 0 HASTA 19 HACER
        suma = suma + lista[i]
        contador = contador + 1
    FIN_PARA
    media = suma / contador
    IMPRIMIR "La media de los números es: ", media
FIN_PROG
"""
import random

lista = [random.randint(1, 100) for i in range(20)]
print("Lista de números aleatorios: ", lista)

suma = 0
contador = 0

for i in range(len(lista)):
    suma += lista[i]
    contador += 1
media = suma / contador
print("La media de los números es: ", media)
