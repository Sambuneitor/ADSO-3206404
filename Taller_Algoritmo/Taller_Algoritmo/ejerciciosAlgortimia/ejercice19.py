"""

Dado un número entero, indicar el número de cifras de ese número (para el 432 debe indicar 3).

------------------------

Ingresar un numero
Contar el número de cifras del número
Mostrar el número de cifras

------------------------

PROG contar_cifras

    numero=INGRESAR("Ingrese un número )
    cifras=0
    
    MIENTRAS numero != 0 HAGA
        numero=numero//10
        cifras=cifras+1
    FIN MIENTRAS
    
    MOSTRAR "El número de cifras es: ", cifras
    

FIN_PROG

"""
while True:
    try:
        numero = int(input("Ingrese un número: "))
        break
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue

cifras = 0

if numero < 0:
    numero = -1*(numero)  # Convertir a positivo si es negativo

numero_str= str(numero)

while cifras != len(numero_str):
    numero = numero // 10
    cifras += 1
    
print(f"El número de cifras es: {cifras}")
    
    