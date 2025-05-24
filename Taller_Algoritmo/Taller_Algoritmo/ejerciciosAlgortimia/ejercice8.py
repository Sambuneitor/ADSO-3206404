"""

Con la lista del ejercicio  6, diseñar una solución que busque el número  mayor y devuelva cuantas 
veces aparece.

------------------------------------

Generar una  lista  de 20  números  enteros  aleatorios  entre  1  y  100.
Buscar el número mayor en la lista.
Buscar cuantas veces aparece el número mayor en la lista.
Mostrar resultado.

------------------------------------

PROG lista_random
    lista = ORDENAR_MAYOR_MENOR(GENERAR 20 numeros aleatorios entre 1 Y 100)

    mayor = 0
    
    SI lista[0] > mayor ENTONCES
        mayor = lista[0]
    FIN_SI
    
    cantidad = CONTAR mayor EN lista
    
    SI cantidad > 0 ENTONCES
        IMPRIMIR "El número mayor es: ", mayor
        IMPRIMIR "El número ", mayor, " aparece ", cantidad, " vez/veces en la lista."
    SINO
        IMPRIMIR "El número ", mayor, " no se encuentra más en la lista."
FIN_PROG

"""

import random

lista = [random.randint(1,100) for i in range(20)]
print("Lista de números aleatorios: ", lista)

lista.sort(reverse=True)
mayor = 0

if lista[0] > mayor:
    mayor = lista[0]
cantidad = lista.count(mayor)

if cantidad > 0:
    print(f"El número mayor es: {mayor}")
    print(f"El número {mayor} aparece {cantidad} vez/veces en la lista.")
