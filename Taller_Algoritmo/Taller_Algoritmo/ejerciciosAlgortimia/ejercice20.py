"""

Calcular los pagos mensuales de una hipoteca y el total a pagar. El programa debe solicitar el capital, 
el interés anual y el número de años y debe escribir la cuota a pagar mensualmente. Para calcular la 
cuota se utiliza la siguiente fórmula: Sea C el capital del préstamo, R la tasa de interés mensual y N 
el número de pagos. La cuota mensual viene dada por: 

cuota = (R*C)/(1-(1/(1+R)**N)), y el interes mensual = interes anual / 100 / 12.

--------------------------

Ingresar capital, interés anual y número de años.
Calcular la cuota.
Mostrar la cuota mensual  y el total a pagar.

-------------------------

PROG hipoteca

    capital = INGRESAR("Ingrese el capital del préstamo: ")
    interes_anual = INGRESAR("Ingrese el interés anual (en %): ")
    numero_anios = INGRESAR("Ingrese el número de años: ")
    
    interes_mensual = interes_anual / 100 / 12
    numero_pagos = numero_anual * 12
    
    cuota = (interes_mensual * capital) / (1 - (1 / (1 + interes_mensual) ** numero_pagos))
    
    total_a_pagar = cuota * numero_pagos
    ESCRIBIR("La cuota mensual a pagar es: ", cuota)
    ESCRIBIR("El total a pagar al final del préstamo es: ", total_a_pagar)

FIN_PROG

"""

while True:
    try:
        capital = float(input("Ingrese el capital del préstamo: "))
        interes_anual = float(input("Ingrese el interés anual (sin necesidad de %): "))
        numero_anios = int(input("Ingrese el número de años: "))
        
        if capital <= 0 or interes_anual < 0 or numero_anios <= 0:
            print("Los valores ingresados deben ser positivos. Intente nuevamente.")
            continue
        
        interes_mensual = interes_anual / 100 / 12
        numero_pagos = numero_anios * 12
        
        cuota = (interes_mensual * capital) / (1 - (1 / (1 + interes_mensual) ** numero_pagos))
        
        total_a_pagar = cuota * numero_pagos
        print(f"La cuota mensual a pagar es: {cuota:.2f}")
        print(f"El total a pagar al final del préstamo es: {total_a_pagar:.2f}")
        
        break
    except ValueError:
        print("Entrada inválida. Por favor, ingrese valores numéricos válidos.")