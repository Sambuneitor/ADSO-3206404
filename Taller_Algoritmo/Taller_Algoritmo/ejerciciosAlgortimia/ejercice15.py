"""

Algoritmo  que  indica  si  un  año  es  bisiesto.  Un  año  es  bisiesto  si  es  divisible  por  cuatro,  excepto cuando es divisible por 100, a no ser que sea divisible por 400. Así, 1900 no fue bisiesto, pero 2000 
sí lo fue.

-------------------------------

Ingresar un año.
Calcular si el año es bisiesto.
Mostrar el resultado.

-------------------------------
PROG bisiesto

    año=INGRESAR "Ingrese un año: "
    
    SI (año MOD 4 = 0) Y (año MOD 100 <> 0) O (año MOD 400 = 0) ENTONCES
        ESCRIBIR "El año ", año, " es bisiesto."
    SINO
        ESCRIBIR "El año ", año, " no es bisiesto."

FIN_PROG
"""
while True:
    try:
        año = int(input("Ingrese un año: "))
        break
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("El año", año, "es bisiesto.")
else:
    print("El año", año, "no es bisiesto.")
    
