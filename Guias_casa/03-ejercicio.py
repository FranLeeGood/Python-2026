# ==============================================================================
# ENUNCIADO: REGISTRO DE CORREOS INSTITUCIONALES (DEPARTAMENTO DE ADMISIÓN)

# Contexto: El Departamento de Admisión de la Universidad requiere un script 
# básico para registrar correos institucionales. El programa debe solicitar al 
# usuario que ingrese su nombre completo por terminal. Debido a que los usuarios 
# pueden escribir con mayúsculas y minúsculas desordenadas o con espacios de más, 
# el programa debe estandarizar el texto.
# ==============================================================================

# a) Solicite por terminal el nombre del estudiante.
nombre_estudiante = str(input("Ingrese su nombre completo"))

# b) Remueva los espacios sobrantes de los extremos.
nombre_sin_espacio = nombre_estudiante.strip()

# c) Convierta todo el texto a minúsculas.
nombre_mayuscula = nombre_sin_espacio.lower()

# d) Reemplace los espacios intermedios por puntos (.) para simular la estructura de
# un correo electrónico.
nombre_sin_punto = nombre_mayuscula.replace(" ",".")

# e) Muestre en pantalla el resultado final con el texto @alumnos.ulagos.cl concatenado
# al final.
print(f"Su correo institucional es {nombre_sin_punto}@alumnos.ulagos.cl")
