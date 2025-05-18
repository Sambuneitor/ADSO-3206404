'''
PROG_EJ4
    INGERESAR num_1

    INGRESAR num_2

        SI num1 > num2 ENTONCES
            temp = num1
            num1 = num2
            num2 = temp

        suma = 0

        Para i desde num_1 HASTA num_2 HAGA
            Si i % 2 = 0 Entonces
                suma += i

        MOSTRAR'La suma de los números pares entre', num1, 'y', num_2, 'es:', suma
FIN_PROG
'''

while True:
    try:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        break
    except:
        print('valor no valido')

if num1 > num2:
    temp = num1
    num1 = num2
    num2 = temp

suma = 0

for i in range(num1, num2 + 1):
    if i % 2 == 0:  
        suma += i

print(f"La suma de los números pares entre {num1} y {num2} es: {suma}")
