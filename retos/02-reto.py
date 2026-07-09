# RETO NUMERO 2
#======================================================================================================
# Estás diseñando el motor de búsqueda de una plataforma educativa para los
# estudiantes de Ingeniería Civil en Informática. El sistema debe almacenar
# conceptos técnicos de Python, permitir búsquedas rápidas, evitar que se
# registren temas duplicados por error y mostrar un reporte final inmutable.
# Para ello, debes programar un código que realice los siguientes pasos:
#======================================================================================================
#1. Evitar duplicados: Un estudiante ayudante ingresó por error una lista de
#conceptos clave donde algunos se repiten:
conceptos_repetidos = ['inmutable', 'iterable', 'inmutable', 'hashable', 'interpretado', 'iterable']

# Debes eliminar automáticamente de alguna manera los duplicados y luego
#transformarlo nuevamente en una lista ordenada.
limpios = list(set(conceptos_repetidos))
conceptos = sorted(limpios)

# 2.Estructurar la base de conocimiento con un Diccionario: Crea un diccionario
#llamado glosario donde las llaves sean los conceptos (los que quedaron tras
#limpiar los duplicados) y los valores sean sus definiciones que se muestra a
#continuación:
glosario = {
    "hashable": "Objeto cuyo valor hash nunca cambia y puede ser clave.",
    "inmutable": "Objeto con un valor fijo que no se puede modificar.",
    "interpretado": "Lenguaje donde el código se ejecuta línea a línea.",
    "iterable": "Objeto capaz de devolver sus elementos uno a la vez."
} 

# 3. Simular el Buscador: Solicita al usuario por consola que ingrese un concepto a
#buscar (asume que el usuario escribirá uno correcto: hashable, inmutable,
#interpretado o iterable).
#Busca la definición directamente en el diccionario e imprime el resultado.
busqueda = input("Concepto a buscar: ")
definicion = glosario[busqueda]
print(definicion)

# 4.Generar un Reporte Inmutable con Tuplas: Para asegurar que los datos del
#reporte final no sufran alteraciones, extrae del diccionario el concepto buscado
#junto a su definición, e insértalos dentro de una Tupla llamada
#registro_busqueda. Imprime en la terminal la tupla del registro para dejar
#constancia de la consulta en el sistema.
registro_busqueda = (busqueda, definicion)
print(registro_busqueda)