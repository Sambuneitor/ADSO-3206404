"""
Diseñar una solución que cree una lista inversa a la dada en 6. Es decir, que genere una nueva lista 
tal que su primer elemento sea el último de la lista inicial, su segundo elemento sea el penúltimo de 
la lista inicial, etc.

-----------------------------------------
PROG lista_random
    lista = GENERAR 20 numeros aleatorios entre 1 Y 100
    
    lista_inversa = []
    
    PARA i DESDE 19 HASTA 0 HACER
        lista_inversa[i] = lista[19-i]
    FIN_PARA
    IMPRIMIR "Lista original: ", lista
    IMPRIMIR "Lista inversa: ", lista_inversa
    
FIN_PROG
"""
import random

lista= [random.randint(1, 100) for i in range(20)]

def invertir_lista(lista):
    lista_inversa = []
    
    for i in range(len(lista) - 1, -1, -1):
        lista_inversa.append(lista[i])
    return lista_inversa
    
print("Lista original: ", lista)

lista_inversa = invertir_lista(lista)
print("Lista inversa: ", lista_inversa)

