'''
PROG_EJ6
    lista = [número aleatorio entre 1 y 20 por 20]

    HACER
        LEER numero
        SI NO es entero ENTONCES IMPRIMIR 'Valor no válido'
    HASTA que sea entero

    encontrado = FALSO
    PARA i DESDE 0 HASTA longitud(lista) - 1 HACER
        SI lista[i] = numero ENTONCES
            IMPRIMIR 'Número encontrado en la posición: ', i
            encontrado = VERDADERO
            ROMPER
        FIN SI
    FIN PARA

    SI NO encontrado ENTONCES IMPRIMIR 'Número no encontrado'

FIN_PROG
'''


import random

lista = [random.randint(1, 20) for _ in range(20)]

while True:
    try:
        numero = int(input('Ingrese un número: '))
        break
    except:
        print('Valor no valido')



encontrado = False
for i in range(len(lista)):
    if lista[i] == numero:
        print(f'Número encontrado en la posición: {i}')
        encontrado = True
        break

if not encontrado:
    print('Número no encontrado')