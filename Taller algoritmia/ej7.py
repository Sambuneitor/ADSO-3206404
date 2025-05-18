'''
PROG_EJ7
    GENERAR lista de 20 números aleatorios entre 1 y 20

    HACER
        INTENTAR
            LEER numero digitado por el usuario
        EXCEPT:
            IMPRIMIR 'Valor no válido'
    HASTA que sea un numero valido

    contador = 0
    posiciones = lista vacía

    PARA cada índice i en la lista
        SI lista[i] es igual a numero ENTONCES
            AGREGAR i a posiciones
            contador = contador + 1

    SI contador > 0 ENTONCES
        IMPRIMIR 'Número encontrado contador veces en las posiciones: posiciones'
    SINO
        IMPRIMIR 'Número no encontrado'
FIN_PROG
'''

import random

lista = [random.randint(1, 20) for _ in range(20)]


while True:
    try:
        numero = int(input('Ingrese un número: '))
        break
    except:
        print('Valor no válido')

contador = 0
posiciones = []

for i in range(len(lista)):
    if lista[i] == numero:
        posiciones.append(i)
        contador += 1

if contador > 0:
    print(f'Número encontrado {contador} veces en las posiciones: {posiciones}')
else:
    print('Número no encontrado') 
