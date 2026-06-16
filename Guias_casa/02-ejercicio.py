# ==============================================================================
# ENUNCIADO: LIMPIEZA DE DATOS (SISTEMA DE BIBLIOTECA ULAGOS)

# Contexto: Al desarrollar sistemas informáticos, los usuarios suelen ingresar 
# datos con espacios accidentales o formatos incorrectos. El sistema de la 
# biblioteca de la ULagos recibió el RUT de un estudiante, pero viene “sucio” 
# con espacios al inicio, al final y con puntos intermedios: " 19.543.872-K ".
# =============================================================================

# a) Guarde el RUT original en una variable de tipo string.
rut_sucio = " 19.543.872-k "

# b) Utilice el método propio de Python para eliminar los espacios en blanco de los
# extremos.
rut_sin_espacio = rut_sucio.strip()

# c) Utilice un método propio de Python para eliminar los puntos (.).
rut_sin_punto = rut_sin_espacio.replace(".","")

# d) Calcule el largo total del RUT ya limpio (sin espacios ni puntos) y muestre el
# resultado por pantalla junto al RUT con su nuevo formato.
largo_rut = len(rut_sin_punto)
print(f"el rut sucio es{rut_sucio} , el rut limpio es {rut_sin_punto} | largo rut: {largo_rut}")