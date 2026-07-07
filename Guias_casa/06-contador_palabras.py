# =============================================================================
# DESCRIPCIÓN DEL EJERCICIO:
# 
# "El Proyecto Integrador del primer semestre, se evaluará y desarrollará en 3 
# asignaturas en conjunto: Taller de Introducción a la Ingeniería donde trabajarán 
# el desarrollo práctico del proyecto, Habilidades Comunicativas donde desarrollarán 
# las habilidades de presentación y redacción y por último Programación, donde 
# aplicarán técnicas para codificar y diseñar el software del proyecto."
#==============================================================================
# REQUISITO ESPECIAL:
# Si el párrafo está vacío, debe lanzar y capturar una excepción (ValueError) 
# indicando "El texto no puede estar vacío".
# =============================================================================
try:
    #a) Lea el párrafo. Este debe ser ingresado por teclado.
    parrafo = input("Ingrese el parrafo de la guia: ")

    if not parrafo.strip():
     raise ValueError ("El texto no puede estar vacio")
    
    print("parrafo ingresado correctamente")

    # b) Separe sus palabras y debe guardarlas en una lista. 
    palabras_lista = tuple(parrafo.split())

    # c) Solicite al usuario una palabra a buscar.
    palabra_buscar = input("Ingrese la palabra que desee buscar: ")

    # d) Imprima cuántas veces aparece dicha palabra (Debe ser sensible a  mayúsculas y minúsculas).
    repeticiones = palabras_lista.count(palabra_buscar)
    print(f"La palabra: {palabra_buscar} aparece: {repeticiones} veces")

except ValueError as e:
    print(f"error: {e}")
