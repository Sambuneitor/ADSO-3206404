"""

------------------------------------------
Ingresar numeros
calcular la suma
mostrar resultado
------------------------------------------
Proceso SumarHastaN
    Definir n, i, suma Como Entero
    suma <- 0

    Repetir
        Escribir "Un número N:"
        Leer n
    Hasta Que n Es Número Entero Válido (esto se maneja con validación en lenguajes reales)

    Para i <- 1 Hasta n Con Paso 1 Hacer
        suma <- suma + i
        Escribir "i =", i
        Escribir "suma =", suma
    FinPara

    Escribir "La suma de todos los números desde 0 hasta", n, "es:", suma
FinProceso
"""

while True:
    try:
        n=int(input("Un numero N: "))
        break
    except:
        print("El dato ingresado no es valido")

suma = 0
for i in range(1,n+1):
    suma+=i

    
print(f"La suma de todos los numeros desde 0 hasta {n} es: ", suma)
    
    
