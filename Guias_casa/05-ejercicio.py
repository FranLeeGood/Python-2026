# ==============================================================================
# ENUNCIADO: RENDIMIENTO DEL SERVIDOR (UNIVERSIDAD DE LOS LAGOS)

# Contexto: Una plataforma web de la Universidad de Los Lagos mide la velocidad 
# de respuesta de su servidor de asignación de asignaturas. Se han tomado 3 
# muestras de tiempo de respuesta (en milisegundos) de forma manual.
# ==============================================================================

# a) Solicite al administrador de la plataforma ingresar por terminal los 3 tiempos de
# respuesta (los cuales pueden contener decimales, tipo float)
toma_respuesta1 = float(input("Ingrese la primera muestra de tiempo"))
toma_respuesta2 = float(input("Ingrese la segunda muestra de tiempo"))
toma_respuesta3 = float(input("Ingrese la tercera muestra de tiempo"))

# b) Almacene los 3 valores ingresados dentro de una lista de Python que debe tener
# por nombre tiempos_respuesta.
tiempo_respuesta = []

# c) Acceda por medio de sus índices ([0], [1], [2]) a los elementos de la lista para
# calcular el tiempo promedio de respuesta del servidor.
tiempo_respuesta.append(toma_respuesta1)
tiempo_respuesta.append(toma_respuesta2)
tiempo_respuesta.append(toma_respuesta3)

suma_tiempos = tiempo_respuesta[0] + tiempo_respuesta[1] + tiempo_respuesta[2]
promedio_tiempo = suma_tiempos / 3

# d) Encuentre el tiempo más rápido (mínimo) y el tiempo más lento (máximo) utilizando 
# las funciones propias de Python.
min_tiempo = min(tiempo_respuesta)
max_tiempo = max(tiempo_respuesta)

# e) Calcule la “brecha de rendimiento”, que corresponde a la resta entre el tiempo
# máximo y el mínimo.
brecha_tiempo = max_tiempo - min_tiempo

# f) Imprima en pantalla la lista completa de datos y el reporte con el promedio y la
# brecha calculada.
print("=====================")
print(f"Lista completa de datos:{tiempo_respuesta}")
print(f"Tiempo promedio de respuesta:{promedio_tiempo:2f}")
print(f"tiempo mas rapido registrado(minimo):{min_tiempo}")
print(f"tiempo mas lento registrado (maximo:{max_tiempo})")
print(f"Brecha de rendimiento(maximo - minimo:{brecha_tiempo:2f})")
print("=====================")