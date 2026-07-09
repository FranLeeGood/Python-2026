# ==============================================================================
# DESCRIPCIÓN DEL EJERCICIO:
# ==============================================================================
# 2. Al procesar bases de datos masivas en proyectos de Ciencia de Datos, es
#    común encontrarse con registros corruptos o mal formateados por los usuarios.
#    El sistema de matrícula ha recibido el código identificador con espacios
#    accidentales y guiones bajos (ejemplo: "  __ICINF-2026_ULA___  ").
# ==============================================================================

# A. Solicite al usuario ingresar el código identificador mediante terminal
codigo_sucio = input("Ingrese el código identificador del estudiante: ")

# B. Elimine todos los espacios en blanco de los extremos usando el método strip
codigo_sin_espacios = codigo_sucio.strip()

# C. Reemplace todos los caracteres de guion bajo (_) por un string vacío ("")
codigo_sin_guiones = codigo_sin_espacios.replace("_", "")

# D. Convierta todo el texto resultante a letras mayúsculas con upper
codigo_limpio = codigo_sin_guiones.upper()

# Calcule el largo total de caracteres del código limpio usando una función para ello (len)
largo_codigo = len(codigo_limpio) 

# E. Despliegue en pantalla un reporte que muestre el código limpio y su longitud
print("\n=========================================")
print("      REPORTE DE LIMPIEZA DE DATOS       ")
print("=========================================")
print(f"Código original ingresado: '{codigo_sucio}'")
print(f"Código identificador limpio: {codigo_limpio}")
print(f"Cantidad de caracteres:      {largo_codigo}")
print("=========================================")
