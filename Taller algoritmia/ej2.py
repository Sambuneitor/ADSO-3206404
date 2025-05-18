'''
PROG_EJ2
    MIENTRAS SEA CIERTO
        INTENTE
            INGRESAR num sea entero
            suma = 0

            PARA i = 1 HASTA num
                suma += 1
            MOSTTRAR 'la suma es: ' suma
            ROMPER
        EXEPCION
            MOSTRAR 'valor no valido'
FIN_PROG
'''


while True:
    try:
        num=int(input('ingrese un numero: '))
        suma=0
        for i in range (1,num + 1):
            suma += i 
        print('la suma es: ', suma)
        break
    except:
        print('valor invalido')
