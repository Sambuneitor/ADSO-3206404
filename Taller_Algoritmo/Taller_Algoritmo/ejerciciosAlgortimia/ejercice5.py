"""

Un algoritmo que dados cinco números los muestre ordenados de mayor a menor.

-----------------------------------------

Ingresar 5 numeros
Operacion de mayor a menor en lista
Mostrar resultado

-----------------------------------------

PROG mayor_a_menor

    lista = []
    i = 0
    
    MIENTRAS i < 5 HACER
        numero=INGRESAR("Ingrese un numero: ")
        lista=AGREGAR(numero)
        i= i + 1
    FIN MIENTRAS
    
    lista=ORDENAR(lista)
    MOSTRAR("Los numeros ordenados de mayor a menor son: ", lista)
    
FIN_PROG

"""

lista = []


while len(lista) < 5:
    
    try:
        numero = int(input("Ingrese un numero: "))
        if numero in lista:
            print("El numero ya fue ingresado, por favor ingrese otro.")
            continue
        lista.append(numero)
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

lista.sort(reverse=True)
print("Los numeros ordenados de mayor a menor son:", lista)
