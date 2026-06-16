#listas 

#primera forma de declaracion de listas 
lista1 = ["francisco", 19,True, 19, "francisco", "francisco"]
ramos = [] #Lista vacia


#segunda forma de declaracion de listas 
n = list([1,2,3,4,5])

#metodos para listas
# imprime el primer elemento de la lista1
print(lista1[0])

#contar la cantidad de concurrencias de un elemento 
print(lista1.count("francisco"))
print(ramos)

#agregar un elemento al final de la lista 
ramos.append("Quimica")
print(ramos)

ramos.append("Habilidades comunicativas")
print(ramos)

ramos.append("Programacion")
print(ramos)

# Otra forma de insertar un elemento a la lista (de forma especifica)
ramos.insert(0, "Introduccion a la matematica")
print(ramos)

# modificar un elemento en especifico de la lista 
ramos[2] = "Habilidades comunicativas para ingenieros"
print(ramos)

# Eliminar el ultimo elemento de la lista 
ramos.pop()
print(ramos)

# Ordenar los elementos de una lista de forma descendente a ascendente 
# print(ramos.sort())
ramos.sort()
print(ramos)

n.sort()
print(n)

# Ordenar elementos de una lista segun la cantidad de caracteres de cada elemento 
ramos.sort (key=len)
print(ramos)

# Extender una lista a partir de otra 
ramos_segundo_semestre = ["Ciudadania" , "Algebra" , "Introduccion a la fisica"]
print (ramos_segundo_semestre)

ramos.extend(ramos_segundo_semestre)
print(ramos)



print(type(n))
print(type(lista1))

#metodos para las listas 

#01-count ()

print(lista1.count("francisco"))

#aplicando metodo de listas 
print(ramos_segundo_semestre.index("algebra"))#posicion 1