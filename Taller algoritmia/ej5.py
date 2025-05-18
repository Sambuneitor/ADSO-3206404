'''
PROG_EJ5
    DECLARAR lista COMO LISTA VACÍA

    PARA i=1 HASTA 5 HACER
        LEER numero COMO ENTERO
        AGREGAR numero A lista
        SALIR DEL BUCLE
        HASTA QUE OCURRA UNA EXCEPCIÓN
        MOSTRAR "Valor no válido."

    ORDENAR lista DE MAYOR A MENOR
    MOSTRAR lista
FIN_PROG
'''


numeros = []

for i in range(5):
    while True:
        try:
            numero = int(input("Ingrese un número: "))
            numeros.append(numero)
            break
        except:
            print('Valor no valido')


numeros.sort(reverse=True)
print(numeros)