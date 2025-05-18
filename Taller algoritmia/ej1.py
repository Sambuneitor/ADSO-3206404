'''
PROG_EJ1
    MIENTRAS se cierto
        INTENTE 
            MOSTRAR num sea entero
            ROMPER
        EXCEPCION
            MOSTRAR 'VALOR NO VALIDO'

    SI num % 2 = 0 ENTONCES
        MOSTRAR 'el numero es par'
    SINO
        MOSTRAR 'el numero es impar'
FIN_PROG
'''


while True:
    try:
        num=int(input("ingrese un numero: "))
        break
    except:
        print("valor no valido")

if num % 2 == 0:
    print('el numero es par')
else:
    print('el numero es impar')