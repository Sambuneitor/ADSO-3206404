"""

Modificar el anterior para que devuelva el número de veces que aparece. 

------------------------------------
PROG lista_random
    lista = GENERAR 20 numeros aleatorios entre 1 Y 100

    número = INGRESAR "UN NÚMERO POR TECLADO"

    SI numero EN lista ENTENCES
        IMPRIMIR "Número encontrado en la posición: ", POSICION(numero)
    SINO
        IMPRIMIR "Número no encontrado"
    FIN_SI
    
    cantidad = CONTAR numero EN lista
    
    SI cantidad > 0 ENTONCES
        IMPRIMIR "El número ", numero, " aparece ", cantidad, " vez/veces en la lista."
    SINO
        IMPRIMIR "El número ", numero, " no se encuentra en la lista."
FIN_PROG
"""
import random

# Generar lista de 20 números aleatorios entre 1 y 100
lista = [random.randint(1, 100) for i in range(20)]
print("Lista de números aleatorios:", lista)

# Validar entrada del usuario
while True:
    opcion = int(input("Ingrese un número entre 1 y 100: "))
    if 1 <= opcion <= 100:
        break
    else:
        print("Número fuera de rango. Intente nuevamente.")

# Contar cuántas veces aparece el número en la lista
cantidad = lista.count(opcion)

if cantidad > 0:
    print(f"El número {opcion} aparece {cantidad} vez/veces en la lista.")
else:
    print(f"El número {opcion} no se encuentra en la lista.")

