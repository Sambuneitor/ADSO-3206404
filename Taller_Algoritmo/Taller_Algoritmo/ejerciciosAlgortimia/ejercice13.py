"""
Integre los ejercicios del 6 al 12, de tal manera que se presente un menú con las diferentes opciones, 
el usuario escogerá una, ejecutando el procedimiento correspondiente y presentando de nuevo el 
menú. Agregue una opción para finalizar la ejecución

------------------------------------------
PROG menu
    IMPRIMIR "1. Generar lista aleatoria"
    IMPRIMIR "2. Ordenar lista de menor a mayor"
    IMPRIMIR "3. Ordenar lista de mayor a menor"
    IMPRIMIR "4. Invertir lista"
    IMPRIMIR "5. Calcular media entre el mayor y el menor"
    IMPRIMIR "6. Salir"
    
    opcion = LEER opcion
    
    HACER
        SEGUN opcion HACER
            1: GENERAR lista aleatoria
            2: ORDENAR lista de menor a mayor
            3: ORDENAR lista de mayor a menor
            4: INVERTIR lista
            5: CALCULAR media entre el mayor y el menor
            6: SALIR
        FIN_SEGUN
        IMPRIMIR "Seleccione una opción:"
        opcion = LEER opcion
    HASTA opcion == 6
"""
import random

def generar_lista_aleatoria():
    lista = [random.randint(1, 100) for _ in range(20)]
    print("Lista de números aleatorios:", lista)
    return lista

def encontrar_numero(lista, opcion):
    print()
    if opcion in lista:
        print("Número encontrado en la posición:", lista.index(opcion))
    else:
        print("Número no encontrado")

def numero_repetido(lista, opcion):
    cantidad = lista.count(opcion)
    print()
    if cantidad > 0:
        print(f"El número {opcion} aparece {cantidad} vez/veces en la lista.")
    else:
        print(f"El número {opcion} no se encuentra en la lista.")

def encontrar_mayor(lista):
    mayor = max(lista)
    cantidad = lista.count(mayor)
    print()
    print(f"El número mayor es: {mayor}")
    print(f"El número {mayor} aparece {cantidad} vez/veces en la lista.")
    return mayor

def aparecer_mas_que_mayor(lista, opcion, mayor):
    contador1 = lista.count(mayor)
    contador2 = lista.count(opcion)
    print()
    if contador2 > contador1:
        print(f"El número {opcion} aparece más veces que el número mayor: {mayor}")
    else:
        print(f"El número {opcion} no aparece más veces que el número mayor: {mayor}")

def media_todos(lista):
    media = sum(lista) / len(lista)
    print()
    print("La media de todos los números es:", media)
    return media

def calcular_media_mayor_menor(lista):
    mayor = max(lista)
    menor = min(lista)
    media = (mayor + menor) / 2
    print()
    print("La media entre el mayor y el menor es:", media)
    return media

def invertir_posiciones(lista):
    lista_inversa = lista[::-1]
    print()
    print("Lista invertida:", lista_inversa)
    return lista_inversa

def menu():
    lista = generar_lista_aleatoria()

    while True:
        try:
            print()
            print(lista)
            print("\nMenú de opciones:")
            print("1. Encontrar número en la lista")
            print("2. Contar número repetido en la lista")
            print("3. Encontrar el número mayor")
            print("4. Verificar si un número aparece más que el mayor")
            print("5. Calcular la media de todos los números")
            print("6. Calcular la media entre el mayor y el menor")
            print("7. Invertir posiciones de la lista")
            print("8. Salir")

            opcion_menu = int(input("Seleccione una opción: "))
            
            if opcion_menu == 1:
                numero = int(input("Ingrese un número entre 1 y 100: "))
                encontrar_numero(lista, numero)

            elif opcion_menu == 2:
                numero = int(input("Ingrese un número entre 1 y 100: "))
                numero_repetido(lista, numero)

            elif opcion_menu == 3:
                encontrar_mayor(lista)

            elif opcion_menu == 4:
                numero = int(input("Ingrese un número entre 1 y 100: "))
                mayor = encontrar_mayor(lista)
                aparecer_mas_que_mayor(lista, numero, mayor)

            elif opcion_menu == 5:
                media_todos(lista)

            elif opcion_menu == 6:
                calcular_media_mayor_menor(lista)

            elif opcion_menu == 7:
                invertir_posiciones(lista)

            elif opcion_menu == 8:
                print("Gracias por usar el programa. Hasta luego.")
                break

            else:
                print("Opción no válida, intente nuevamente.")

        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

menu()

