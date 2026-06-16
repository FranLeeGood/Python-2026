# TUPLAS 

estudiantes = ("Matias", "Franscisco", "Alan", "Maykol")
print(type(estudiantes))

# Creando una tupla compleja con datos estructurados
datos = ([1,2,3,4,5], ("Queilen", "Castro"), ("Universidad de Los Lagos", "AIEP"))

# Tambien se puede consultar la posicion de un elemento al igual que la lista
print(datos[0])
print(datos)

# Con las listas se pueden eliminar elementos
lista_asignaturas =['Programacion', 'Quimica', 'Introduccion ']
print(f"LISTA: {lista_asignaturas}")

#No se puede eliminar con pop una tupla porque es inmutable
#lista_asignaturas.pop()
#print(f"LISTA CON ELEMENTO ELIMINADO: {lista_asignaturas}")""""

print(estudiantes.index("Alan")) #se encuentra en la posicion 2
print(sorted(estudiantes))