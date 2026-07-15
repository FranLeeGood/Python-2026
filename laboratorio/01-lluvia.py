# ==============================================================================
# DESCRIPCIÓN DEL EJERCICIO:
# ==============================================================================
# 1. Una estación meteorológica ubicada en las cercanías de la Sede de la Univer-
#    sidad de Los Lagos en Castro registra la cantidad de lluvia caída (medida en
#    milímetros, mm) en diferentes momentos de un sistema frontal.
# ==============================================================================

# A. Solicitar al usuario ingresar por terminal las muestras (guardadas como float)
print("--- Ingreso de datos meteorológicos ---")
muestra1 = float(input("Ingrese la primera muestra de lluvia (mm): "))
muestra2 = float(input("Ingrese la segunda muestra de lluvia (mm): "))
muestra3 = float(input("Ingrese la tercera muestra de lluvia (mm): "))

# B. Almacene de forma ordenada estos valores dentro de una lista llamada registro_lluvia
registro_lluvia = [muestra1, muestra2, muestra3]

# C. Acceda de manera directa a los elementos de la lista mediante sus índices fijos
#    ([0], [1], [2]) para calcular el promedio
suma = registro_lluvia[0] + registro_lluvia[1] + registro_lluvia[2]
promedio = suma / 3
 
# D. Identifique el registro más bajo y más alto utilizando funciones integradas (min y max)
#    Calcule la "brecha pluvial" restando el máximo menos el mínimo
minimo = min(registro_lluvia)
maximo = max(registro_lluvia)
brecha_pluvial = maximo - minimo

# E. Imprima un informe técnico por pantalla con todos los resultados obtenidos
print("\n=========================================")
print("           INFORME TÉCNICO               ")
print("=========================================")
print(f"Lista completa de datos registrados: {registro_lluvia} mm")
print(f"Promedio de precipitaciones caídas:  {promedio:.2f} mm")
print(f"Registro de lluvia mínimo:           {minimo} mm")
print(f"Registro de lluvia máximo:           {maximo} mm")
print(f"Brecha pluvial de la tormenta:       {brecha_pluvial:.2f} mm")
print("=========================================")

