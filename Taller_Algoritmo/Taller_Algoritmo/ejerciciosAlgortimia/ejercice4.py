"""
Diseñar el algoritmo que calcule la suma de los pares que hay entre dos números dados.

---------------------------------

PROG suma_pares

    num1=INGRESAR("Ingrese el primer número:")
    num2=INGRESAR("Ingrese el segundo número:")
    
    SI num1 > num2 ENTONCES
        menor = num2
        mayor = num1
    SINO
        menor = num1
        mayor = num2
    FIN SI
    
    suma = 0
    
    PARA i = menor + 1 HASTA mayor - 1 HACER
        SI i MOD 2 = 0 ENTONCES
            suma = suma + i
        FIN SI
    FIN PARA
    
    MOSTRAR "La suma de los números pares entre", menor, "y", mayor, "es:", suma
    
FIN_PROG
"""

while True:
    try:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        break
    except ValueError:
        print("Por favor, ingrese números enteros válidos. Porque: ", ValueError)
        
if num1 > num2:
    menor = num2
    meyor = num1
else:
    menor = num2
    mayor = num1
    
suma=0
for i in range(menor+1, mayor):
    if i % 2 == 0:
        suma=suma+i

print(f"La suma de los numeros pares entre {menor} y {mayor} es: {suma}")

