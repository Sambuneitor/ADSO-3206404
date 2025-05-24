"""

Escriba  un  algoritmo  que  calcule  la  letra  de  control  para  el  NIT.  Se  pedirá  el  NIT  y  escribirá  por 
pantalla  la  letra  correspondiente.  Para  calcularlo,  se  obtiene  el  resto  de  dividir  el  número  de  NIT 
entre 23, y se utiliza la siguiente tabla: 

PROG nit

    nit=INGRESAR ("Ingrese el NIT: ")
    
    resto= nit MOD 23
    
    tabla = {
        0 : "T",
        1 : "R",
        2 : "W",
        3 : "A",
        4 : "G",
        5 : "M",
        6 : "Y",
        7 : "F",
        8 : "P",
        9 : "D",
        10 : "X",
        11 : "B",
        12 : "N",
        13 : "J",
        14 : "Z",
        15 : "S",
        16 : "Q",
        17 : "V",
        18 : "H",
        19 : "L",
        20 : "C",
        21 : "K",
        22 : "E"
    }
    letra_control = tabla[resto]
    
    IMPRIMIR "La letra de control para el NIT", nit, "es:", letra_control

FIN_PROG
"""

while True:
    try:
        nit = int(input("Ingrese el NIT: "))
        if nit < 0:
            raise ValueError("El NIT no puede ser negativo.")
        break
    except ValueError as e:
        print(f"Error: {e}. Por favor, ingrese un número entero positivo.")
        
resto = nit % 23

tabla = {
    0: "T",
    1: "R",
    2: "W",
    3: "A",
    4: "G",
    5: "M",
    6: "Y",
    7: "F",
    8: "P",
    9: "D",
    10: "X",
    11: "B",
    12: "N",
    13: "J",
    14: "Z",
    15: "S",
    16: "Q",
    17: "V",
    18: "H",
    19: "L",
    20: "C",
    21: "K",
    22: "E"
}
letra_control = tabla[resto]
print(f"La letra de control para el NIT {nit} es: {letra_control}")