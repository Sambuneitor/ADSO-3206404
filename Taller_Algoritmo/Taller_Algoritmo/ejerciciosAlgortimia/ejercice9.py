"""

Con la lista del ejercicio 6, diseñar una solución que devuelva Verdadero si el número leído aparece 
más veces que el mayor.

-----------------------------------------

Generar una  lista  de 20  números  enteros  aleatorios  entre  1  y  100.
Luego, leer un número por teclado y determinar si el número leído se encuentra en la lista.
Determinar el numero mayor de la lista.
Determinar si el numero leido aparece más veces que el leido que el mayor.
Mostrar el resultado.

-----------------------------------------
PROG lista_random
    lista = ORDENAR_MAYOR_A_MENOR(GENERAR 20 numeros aleatorios entre 1 Y 100)

    número = INGRESAR "UN NÚMERO POR TECLADO"
    SI número < 1 O número > 100 ENTONCES
        IMPRIMIR "Número fuera de rango. Intente nuevamente."
    SINO numero NO EN lista
        IMPRIMIR "Número no encontrado"
    FIN_SI
    
    
    mayor = 0
    
    SI lista[0] > mayor ENTONCES
        mayor = lista[0]
    FIN_SI
    
    contador1= CONTAR mayor EN lista
    contador2= CONTAR numero EN lista
    
    SI contador2 > contador1 ENTONCES
        IMPRIMIR "El número ", numero, " aparece más veces que el número mayor: ", mayor
    SINO
        IMPRIMIR "El número ", numero, " no aparece más veces que el número mayor: ", mayor
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
        if opcion in lista:
            print("Número encontrado en la posición: ", lista.index(opcion))
        else:
            print("Número no encontrado")
    else:
        break

mayor = 0

if lista[0] > mayor:
    mayor = lista[0]
    
contador1 = lista.count(mayor)
contador2 = lista.count(opcion)

if contador2 > contador1:
    print(f"El número {opcion} aparece más veces que el número mayor: {mayor}")
elif contador2 == contador1:
    print(f"El número {opcion} aparece la misma cantidad de veces que el número mayor: {mayor}")
else:
    print(f"El número {opcion} no aparece más veces que el número mayor: {mayor}")