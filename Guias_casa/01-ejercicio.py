# ==============================================================================
# ANÁLISIS DE IMPEDANCIA EN REDES DE TELECOMUNICACIONES

# Contexto: En el análisis de antenas y redes de telecomunicaciones, la 
# impedancia de una línea de transmisión se compone de una parte real 
# (resistencia) y una parte imaginaria (reactancia). Un ingeniero necesita 
# calcular la impedancia total sumando los componentes de dos tramos de la 
# red de fibra óptica de la universidad.
# ==============================================================================

# a) Defina la impedancia del Tramo 1 como un número complejo con parte real 50 y
# parte imaginaria 30 (50 + 30j).
tramo1 = 50 + 30j

# b) Defina la impedancia del Tramo 2 de la misma forma, con parte real 40 y parte
# imaginaria −10 (40 − 10j).
tramo2 = 40 - 10j

# c) Calcule la impedancia total sumando ambos tramos.
impedancia_total = tramo1 + tramo2
print (f"La imedancia total de los dos tramos es{impedancia_total}")

# d) Muestre en pantalla la impedancia total, y luego imprima por separado solo la
# parte real (convertida a número entero int) y la parte imaginaria (convertida a
# int) usando los atributos .real y .imag.
parte_real = int(impedancia_total.real)
parte_imaginaria = int(impedancia_total.imag)
print(f"La impedancia total real es {parte_real}")
print(f"La impedancia imaginaria total es {parte_imaginaria}")


