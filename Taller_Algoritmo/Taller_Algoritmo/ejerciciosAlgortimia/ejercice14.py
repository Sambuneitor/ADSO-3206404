"""
Diseñar un algoritmo que cuente el número de palabras de un texto y el tamaño de la palabra más 
grande. Una palabra puede venir separada de otra únicamente por un espacio. El texto se ingresará 
por teclado.

-------------------------------
PROG contador

    texto=INGRESAR "Ingrese un texto: "
    palabras=0
    max=0
    palabra=0
    i=0
    longitud=LONGITUD(texto)
    
    MIENTRAS i< longitud HACER
        SI texto[i] = " " ENTONCES
            palabras=palabras+1
            SI palabra>max ENTONCES
                max=palabra
            FIN SI
            palabra=0
        SINO
            palabra=palabra+1
        FIN SI
        i=i+1
    FIN MIENTRAS
    SI palabra>max ENTONCES
        max=palabra
    FIN SI
    palabras=palabras+1
    ESCRIBIR "El tamaño de la palabra más grande es: ", max
    ESCRIBIR "El número de palabras del texto es: ", palabras

FIN_PROG

"""

texto=str(input("Ingrese un texto: "))

palabras=0
max=0
palabra=0
longitud=len(texto)

for i in range(longitud):
    if texto[i] == " ":
        palabras+=1
        if palabra>max:
            max=palabra
        palabra=0
    else:
        palabra+=1
        
if palabra>max:
    max=palabra
palabras+=1
print("El tamaño de la palabra más grande es:", max)
print("El número de palabras del texto es:", palabras)

