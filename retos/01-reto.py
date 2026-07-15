# RETO NUMERO 1
#====================================================================================
# En la asignatura de Programación de la carrera de Ingeniería Civil en Informática,
# un estudiante ha rendido sus primeras 3 calificaciones de tareas prácticas de
# laboratorio. La aprobación de la asignatura exige calcular una nota final basada
# en los siguientes pesos o ponderaciones para cada laboratorio:
#====================================================================================
# • Laboratorio 1: 40% de la nota final
# • Laboratorio 2: 40% de la nota final
# • Laboratorio 3: 20% de la nota final
#====================================================================================
# Se solicita construir un programa en Python que realice las siguientes acciones:

# 1.Solicitar al usuario por terminal el ingreso de las 3 notas individualmente
#  (estas notas deben n incluir decimales).
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))

# 2.Almacenar las 3 notas dentro de una estructura de datos de tipo lista.
notas = [n1, n2, n3]

# 3.Calcular el promedio ponderado final. Para esto, debes extraer las notas
#  directamente desde la lista utilizando sus índices (posiciones) y multiplicarlas
#  por sus respectivos porcentajes antes de sumarlas.
promedio = (notas[0] * 0.40) + (notas[1] * 0.40) + (notas[2] * 0.20)

# 4.Mostrar en la terminal un reporte con todas las notas y el promedio final.
print("--- REPORTE ---") 
print("Lab 1:", notas[0])
print("Lab 2:", notas[1])
print("Lab 3:", notas[2])
print("Promedio Final:", round(promedio, 2))


