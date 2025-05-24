"""

Escribir  el  algoritmo  que  devuelve  el  cambio  de  las  máquinas  de  la  cafetería.  La  máquina  solo 
devuelve  monedas  de  1000,  500,  200,  100,  50.  Se  debe  ingresar  el  valor  a  cobrar  y  el  monto 
entregado.

-------------------------------

Ingresar el valor a cobrar
Operación de cambio
Mostrar el cambio

-------------------------------

PROG cambio
    cobrar=INGRESAR "Ingrese el valor a cobrar: "
    entregado=INGRESAR "Ingrese el monto entregado: "
    cambio=entregado-cobrar
    monedas1000=0
    monedas500=0
    monedas200=0
    monedas100=0
    monedas50=0
    
    SI cambio<0 ENTONCES
        ESCRIBIR "El monto entregado es menor al valor a cobrar."
    SINO
        MIENTRAS cambio>0 HACER
            SI cambio>=1000 ENTONCES
                monedas1000=cambio DIV 1000
                cambio=cambio MOD 1000
            SINO SI cambio>=500 ENTONCES
                monedas500=cambio DIV 500
                cambio=cambio MOD 500
            SINO SI cambio>=200 ENTONCES
                monedas200=cambio DIV 200
                cambio=cambio MOD 200
            SINO SI cambio>=100 ENTONCES
                monedas100=cambio DIV 100
                cambio=cambio MOD 100
            SINO SI cambio>=50 ENTONCES
                monedas50=cambio DIV 50
                cambio=cambio MOD 50
            FIN SI
        FIN MIENTRAS
        
        ESCRIBIR "El cambio es: "
        ESCRIBIR "Monedas de 1000: ", monedas1000
        ESCRIBIR "Monedas de 500: ", monedas500
        ESCRIBIR "Monedas de 200: ", monedas200
        ESCRIBIR "Monedas de 100: ", monedas100
        ESCRIBIR "Monedas de 50: ", monedas50
FIN_PROG

"""

# Ingresar el valor a cobrar
cobrar = int(input("Ingrese el valor a cobrar: "))
# Ingresar el monto entregado
entregado = int(input("Ingrese el monto entregado: "))
# Calcular el cambio
cambio = entregado - cobrar
# Inicializar las variables de monedas
monedas1000 = 0
monedas500 = 0
monedas200 = 0
monedas100 = 0
monedas50 = 0
# Verificar si el cambio es negativo
if cambio < 0:
    print("El monto entregado es menor al valor a cobrar.")
else:
    
    # Calcular el cambio
    while cambio > 0:
        if cambio >= 1000:
            monedas1000 = cambio // 1000
            cambio = cambio % 1000
        elif cambio >= 500:
            monedas500 = cambio // 500
            cambio = cambio % 500
        elif cambio >= 200:
            monedas200 = cambio // 200
            cambio = cambio % 200
        elif cambio >= 100:
            monedas100 = cambio // 100
            cambio = cambio % 100
        elif cambio >= 50:
            monedas50 = cambio // 50
            cambio = cambio % 50

    # Mostrar el resultado
    print("El cambio es: ")
    print("Monedas de 1000:", monedas1000)
    print("Monedas de 500:", monedas500)
    print("Monedas de 200:", monedas200)
    print("Monedas de 100:", monedas100)
    print("Monedas de 50:", monedas50)