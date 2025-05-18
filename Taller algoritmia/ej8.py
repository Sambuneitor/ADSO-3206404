'''
PROG_EJ8
    lista = GENERAR_LISTA_ALEATORIA(20, 1, 20)
    IMPRIMIR "Lista: ", lista

    REPETIR
        IMPRIMIR "Ingrese un número: "
        numero = LEER_ENTRADA()
    HASTA QUE numero SEA ENTERO

    encontrado = FALSO
    PARA i EN rango(lista) HACER
        SI lista[i] IGUAL A numero ENTONCES
            IMPRIMIR "Encontrado en: ", i
            encontrado = VERDADERO
            SALIR
        FIN SI
    FIN PARA

    SI NO encontrado ENTONCES
        IMPRIMIR "No encontrado"

    numero_mayor = MAXIMO(lista)
    contador = CONTAR(lista, numero_mayor)
    IMPRIMIR "Mayor: ", numeromayor, " veces: ", contador

FIN_PROG
'''

import random

lista = [random.randint(1, 20) for _ in range(20)]

print(f'Lista generada: {lista}')

while True:
    try:
        numero = int(input('Ingrese un número: '))
        break
    except:
        print('Valor no válido, por favor ingrese un número entero.')

encontrado = False
for i in range(len(lista)):
    if lista[i] == numero:
        print(f'Número encontrado en la posición: {i}')
        encontrado = True
        break

if not encontrado:
    print('Número no encontrado')

numero_mayor = max(lista)

contador = lista.count(numero_mayor)

print(f'El número mayor es {numero_mayor} y aparece {contador} veces en la lista.')