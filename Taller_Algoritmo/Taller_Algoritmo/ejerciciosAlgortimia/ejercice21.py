"""

Juego del Rojo-amarillo-verde:

El programa genera tres dígitos aleatorios distintos entre 0 y 9. A estos dígitos se les asignan las posiciones 1, 2 y 3.

El objetivo del juego es adivinar los dígitos, así como sus posiciones correctas en el menor número de intentos posibles.

Para cada intento, el jugador proporciona tres dígitos para las posiciones 1, 2, y 3. El programa responde con una pista que consta de rojo, amarillo y verde. 

Si un dígito adivinado está en la posición correcta la respuesta es verde. Si el digito adivinado está en posición incorrecta, la respuesta es amarillo. Si el dígito para una posición dada no coincide con ninguno de los tres dígitos, la respuesta es rojo.

--------------------------

Generar tres dígitos aleatorios distintos entre 0 y 9 en las posiciones 1, 2 y 3.
Ingresar numero del digito y la posicion.
Comparar el numero ingresado con los numeros generados y dar la respuesta correspondiente o pistas.
Calcular el numero ingresado y la posición.
Mostrar el resultado de cada intento.

--------------------------


"""
import random

lista = random.sample(range(10), 3)

intentos = 0

while True:
    intentos += 1
    print(f"Intento {intentos}:")
    
    try:
        digito1 = int(input("Ingrese el dígito para la posición 1: "))
        digito2 = int(input("Ingrese el dígito para la posición 2: "))
        digito3 = int(input("Ingrese el dígito para la posición 3: "))
    except ValueError:
        print("Entrada inválida. Por favor, ingrese números enteros.")
        continue

    respuesta = []
    
    # Verificar cada dígito y su posición
    for i, digito in enumerate([digito1, digito2, digito3]):
        if digito == lista[i]:
            respuesta.append("verde")
        elif digito in lista:
            respuesta.append("amarillo")
        else:
            respuesta.append("rojo")
    
    print("Respuesta:", respuesta)
    
    if respuesta == ["verde", "verde", "verde"]:
        print(lista)
        print(f"¡Felicidades! Adivinaste los números en {intentos} intentos.")
        break
