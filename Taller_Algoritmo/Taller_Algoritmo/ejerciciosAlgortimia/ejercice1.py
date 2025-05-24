"""
--------------------------------
    Ingresar numero
    Operacion si es par o impar
    Mostrar resultado
--------------------------------
PROG parOimpar

    MIENTRAS repetir = 1 HAGA
        numero=INGRESAR "Ingresar un numero entero: "
        SI numero es menor a 0 HAGA
            MOSTRAR "El numero debe ser positico"
        SINO HAGA
            repetir=0
        FIN_SI
    FIN_MIENTRAS
    
    SI numero %2 = 0 ENTONCES
        MOSTRAR "El numro es par"
    SINO HAGA
        MOSTRAR "El numero es impar"
    FIN_SI
    
    
    
FIN_PROG
"""
while True:
    try:
        numero=int(input("Un numero entero: "))
        break
    except:
        print("El dato ingresado no es valido")
        
if numero %2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")