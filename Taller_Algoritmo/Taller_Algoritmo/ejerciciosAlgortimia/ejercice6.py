"""

Dada  en  una  lista  no  ordenada  de  números  (20  enteros  generados  aleatoriamente)  y  un  número 
leído por teclado, diseñar una solución que busque en la lista el número leído. Si lo encuentra, debe 
informar su posición en la lista, sino debe devolver la frase “Número no encontrado”. 

-----------------------------------------
PROG lista_random
    lista = GENERAR 20 numeros aleatorios entre 1 Y 100

    número = INGRESAR "UN NÚMERO POR TECLADO"

    SI numero EN lista ENTENCES
        IMPRIMIR "Número encontrado en la posición: ", POSICION(numero)
    SINO
        IMPRIMIR "Número no encontrado"
    FIN_SI
FIN_PROG
"""

import random

lista=[random.randint(1,100) for i in range(20)]
print("Lista de números aleatorios: ", lista)

while True:
    opcion = int(input("Ingrese un número entre 1 y 100: "))
    if opcion < 1 or opcion > 100:
        print("Número fuera de rango. Intente nuevamente.")
    else:
        break
if opcion in lista:
    print("Número encontrado en la posición: ", lista.index(opcion))
else:
    print("Número no encontrado")
    