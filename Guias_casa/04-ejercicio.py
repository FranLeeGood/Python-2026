# ==============================================================================
# ENUNCIADO: PRECISIÓN DE DATOS EN FÍSICA DE PARTÍCULAS

# Contexto: En física de partículas, la precisión de los decimales es crítica. 
# Un sensor de presión hidráulica en un laboratorio de la universidad entrega 
# una medida de 1024.7689 Pascales como tipo float.
# ==============================================================================

# a) Defina la variable con el valor del sensor.
valor_sensor = 1024.7689


# b) Convierta dicho valor a un número entero (int), descartando los decimales, y
# almacénelo en una variable nueva
sensor_nuevo = int(valor_sensor)

# c) Utilice un método propio de Python para redondear el valor original del sensor a
# exactamente 2 decimales y guarde el resultado en otra variable
redondeo_valor = round(valor_sensor,2)

# d) Imprima un mensaje comparativo que muestre por terminal: el valor original, el
# valor truncado como entero y el valor redondeado.
print(f"El valor original es:{valor_sensor} | el valor entero es:{sensor_nuevo} | el valor redondeado es:{redondeo_valor}")


