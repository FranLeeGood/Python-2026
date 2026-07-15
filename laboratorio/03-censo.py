# ==============================================================================
# REQUERIMIENTO A: Crear el diccionario inicial 'censo_2017'
# ==============================================================================
# Las claves son los IDs de las regiones como enteros (int).
# Los valores son sub-diccionarios con la información de la Tabla N°1.
censo_2017 = {
    14: {
        "Nombre Región": "Los Ríos",
        "Superficie": 18429,
        "Habitantes": 404432
    },
    12: {
        "Nombre Región": "Magallanes",
        "Superficie": 1382291,
        "Habitantes": 166533
    }
}

print("--- REQUERIMIENTO A: Diccionario Inicial ---")
print(censo_2017)
print("-" * 50)


# ==============================================================================
# REQUERIMIENTO B: Calcular la Densidad Poblacional usando un bucle
# ==============================================================================
# Iteramos sobre cada región del diccionario para calcular la densidad.
# Densidad = Habitantes / Superficie (Redondeado a 1 decimal).
for id_region, datos in censo_2017.items():
    habitantes = datos["Habitantes"]
    superficie = datos["Superficie"]
    
    # Calculamos y redondeamos a 1 decimal
    densidad_calculada = round(habitantes / superficie, 1)
    
    # Añadimos la nueva clave al sub-diccionario
    datos["Densidad"] = densidad_calculada


# ==============================================================================
# REQUERIMIENTO C: Agregar datos complementarios de la Tabla N°2
# ==============================================================================
# Agregamos Capital (str), Comunas (lista), Coordenadas (tupla) y Zonas (set)

# Datos para Los Ríos (ID 14)
censo_2017[14]["Capital"] = "Valdivia"
censo_2017[14]["Comunas"] = ["Río Bueno", "La Unión", "Paillaco"]
censo_2017[14]["Coordenadas_Simuladas"] = (-39.8, -73.2)
censo_2017[14]["Zonas_Exclusivas"] = {"Urbana", "Rural", "Fronteriza"}

# Datos para Magallanes (ID 12)
censo_2017[12]["Capital"] = "Punta Arenas"
censo_2017[12]["Comunas"] = ["Cabo de Hornos", "Puerto Williams", "Porvenir"]
censo_2017[12]["Coordenadas_Simuladas"] = (-53.1, -70.9)  # Coordenadas ficticias para Magallanes
censo_2017[12]["Zonas_Exclusivas"] = {"Urbana", "Rural", "Costera"}


# ==============================================================================
# REQUERIMIENTO D: Actualizar el nombre de la región 12 obligatoriamente
# ==============================================================================
# Pasará de "Magallanes" a "Magallanes y Antártica Chilena"
censo_2017[12]["Nombre Región"] = "Magallanes y Antártica Chilena"


# ==============================================================================
# REQUERIMIENTO E: Menú interactivo con bucle (while)
# ==============================================================================
# Permite consultar comunas ingresando el ID de la región. Termina con "salir" o 0.
print("--- REQUERIMIENTO E: Menú Interactivo de Consultas ---")

while True:
    entrada = input("Ingrese el ID de la región a consultar (12 o 14) o 'salir'/0 para terminar: ")
    
    # Condición de salida (si escribe 'salir' o '0')
    if entrada.lower() == "salir" or entrada == "0":
        print("Saliendo del menú de consultas...")
        break
    
    # Validamos si la entrada es un número para buscarlo en el diccionario
    if entrada.isdigit():
        id_ingresado = int(entrada)
        
        # Si el ID existe en nuestro diccionario (12 o 14)
        if id_ingresado in censo_2017:
            nombre_reg = censo_2017[id_ingresado]["Nombre Región"]
            lista_comunas = censo_2017[id_ingresado]["Comunas"]
            print(f"Las comunas sugeridas para la región de {nombre_reg} son: {lista_comunas}\n")
        else:
            print("Error: El ID ingresado no existe en el registro. Intente nuevamente.\n")
    else:
        print("Error: Entrada no válida. Ingrese un ID numérico (12 o 14), 'salir' o 0.\n")
 
print("-" * 50)


# ==============================================================================
# REQUERIMIENTO F: Imprimir lista de tuplas fuera del menú
# ==============================================================================
# Utilizamos el método .items() para obtener la clave y el valor de cada elemento principal
lista_final_tuplas = list(censo_2017.items())

print("--- REQUERIMIENTO F: Lista Final de Tuplas (.items) ---")
for elemento in lista_final_tuplas:
    print(elemento)

