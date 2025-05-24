"""

Con la lista del ejercicio 6, Diseñar una solución que calcule la media entre el mayor y el menor. 

------------------------------------------

Generar una  lista  de 20  números  enteros  aleatorios  entre  1  y  100.
Calcular la media entre el mayor y el menor.
Mostrar el resultado.

-----------------------------------------
PROG lista_random
    lista = GENERAR 20 numeros aleatorios entre 1 Y 100

    mayor = lista[0]
    menor = lista[0]
    PARA i DESDE 1 HASTA 19 HACER
        SI lista[i] > mayor ENTONCES
            mayor = lista[i]
        FIN_SI
        SI lista[i] < menor ENTONCES
            menor = lista[i]
        FIN_SI
    FIN_PARA
    media = (mayor + menor) / 2
    IMPRIMIR "La media entre el mayor y el menor es: ", media
FIN_PROG

"""

import random

lista = [random.randint(1, 100) for i in range(20)]
print("Lista de números aleatorios: ", lista)

mayor = lista[0]
menor = lista[0]

for i in range(1, len(lista)):
    if lista[i] > mayor:
        mayor = lista[i]
    if lista[i] < menor:
        menor = lista[i]
        
media = (mayor + menor) / 2
print("La media entre el mayor y el menor es: ", media)