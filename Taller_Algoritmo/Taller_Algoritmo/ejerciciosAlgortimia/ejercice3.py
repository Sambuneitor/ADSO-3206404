"""

    Diseñar el algoritmo que encuentre (muestre) los números pares que hay entre el 100 y el 1000. 
    
-------------------------------------------

Definir variables
Operacion par encontrar pares
Muestra resultado

-------------------------------------------
PROG pares

    PARA i = 100 HASTA 1000
        SI numero MOD 2 = 0 Entonces
            Escribir numero
        FIN_SI
    FIN_PARA
FIN_PROG

"""
for i in range(100, 1001,2):  # Desde 100 hasta 1000 (inclusive)
    print(i, end=", ")
"""    if i % 2 == 0:
        print(i)"""

