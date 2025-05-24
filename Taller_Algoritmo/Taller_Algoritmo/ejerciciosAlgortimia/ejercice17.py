"""

En Tecnólogo de ADSO del SENA hay 10 aprendices matriculados, pero acaba de un nuevo aprendiz 
que  se  incorporará  a  formación.  El  listado  de  aprendices  se  encuentra  ordenado  alfabéticamente 
por apellido. Ahora hay que incluir al nuevo aprendiz en la lista (mostrar la lista antes y después de 
ingresar al nuevo aprendiz). 

--------------------------------

Lista de arendices
Ingresar apellido del nuevo aprendiz
Ordenar la lista de forma alfabetica
Mostrar la lista antes y después de agregar el nuevo aprendiz

--------------------------------

PROG lista_aprendices

    aprendices = ["Gonzalez", "Lopez", "Martinez", "Perez", "Rodriguez", "Sanchez", "Torres", "Vasquez", "Zapata"]
    
    nuevo_aprendiz = INGRESAR "Ingrese el apellido del nuevo aprendiz: "
    
    aprendices.append(nuevo_aprendiz)
    aprendices.sort()
    
    ESCRIBIR "Lista de aprendices antes de agregar el nuevo aprendiz: "
    
    PARA cada aprendiz EN aprendices HACER
        ESCRIBIR aprendiz
    FIN PARA
    
    ESCRIBIR "Lista de aprendices después de agregar el nuevo aprendiz: "
    
FIN_PROG

"""

# Definición de la lista de aprendices
aprendices = ["Gonzalez", "Lopez", "Martinez", "Perez", "Rodriguez", "Sanchez", "Torres", "Vasquez", "Zapata"]

# Mostrar la lista de aprendices antes de agregar el nuevo aprendiz
print("Lista de aprendices antes de agregar el nuevo aprendiz:")

for aprendiz in aprendices:
    print(aprendiz)
    
# Solicitar el apellido del nuevo aprendiz
nuevo_aprendiz = input("Ingrese el apellido del nuevo aprendiz: ")

# Agregar el nuevo aprendiz a la listaa"]
aprendices.append(nuevo_aprendiz)
aprendices.sort()

# Mostrar la lista de aprendices después de agregar el nuevo aprendiz
print("\nLista de aprendices después de agregar el nuevo aprendiz: ", aprendices)

