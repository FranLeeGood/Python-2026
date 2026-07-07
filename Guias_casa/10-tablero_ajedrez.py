# ==============================================================================
# DESCRIPCIÓN DEL EJERCICIO:
# ==============================================================================
# 5. Escribir un programa que simule el movimiento de piezas en un tablero de ajedrez,
#    mostrando gráficamente el estado del tablero (por consola) y registrando las 
#    piezas capturadas.
#
#    a) Inicialización del tablero (Coordenadas "a1"..."h8" con sufijo "B" o "N").
#    b) Mapa de símbolos ASCII para representación gráfica.
#    c) Mostrar el tablero dibujado en consola con filas (8 a 1) y columnas (a a h).
#    d) Interacción con el usuario (Listar capturas e ingresar casillas origen/destino).
#    e) Lógica de movimiento (Validaciones de existencia y captura de enemigas).
#    f) Reporte tras cada turno (Redibujar tablero y lista de capturas en ASCII).
# ==============================================================================

# ==============================================================================
# a) Inicialización del tablero
# ==============================================================================
# Creamos el diccionario base con todas las posiciones vacías usando bucles anidados
tablero = {}
columnas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for fila in range(1, 9):
    for col in columnas:
        tablero[f"{col}{fila}"] = "."

# Instanciamos las piezas fijas (Hardcodeado) en la Fila 1 (Blancas) y Fila 8 (Negras)
piezas_fila1 = ["TorreB", "CaballoB", "AlfilB", "ReinaB", "ReyB", "AlfilB", "CaballoB", "TorreB"]
piezas_fila8 = ["TorreN", "CaballoN", "AlfilN", "ReinaN", "ReyN", "AlfilN", "CaballoN", "TorreN"]

for i, col in enumerate(columnas):
    tablero[f"{col}1"] = piezas_fila1[i]
    tablero[f"{col}8"] = piezas_fila8[i]
    tablero[f"{col}2"] = "PeonB"
    tablero[f"{col}7"] = "PeonN"


# ==============================================================================
# b) Mapa de símbolos ASCII
# ==============================================================================
# Diccionario que asocia el nombre técnico de la pieza con su carácter en la consola
simbolos = {
    ".": ".",
    "TorreB": "R", "CaballoB": "N", "AlfilB": "B", "ReinaB": "Q", "ReyB": "K", "PeonB": "P",
    "TorreN": "r", "CaballoN": "n", "AlfilN": "b", "ReinaN": "q", "ReyN": "k", "PeonN": "p"
}


# ==============================================================================
# d) Interacción con el usuario - Variables Iniciales
# ==============================================================================
# Declaración de la lista vacía donde se almacenarán las piezas enemigas capturadas
lista_capturadas = []

# Iniciamos el bucle del juego interactivo
jugando = True
while jugando:
    
    # ==========================================================================
    # c) Mostrar el tablero dibujado
    # ==========================================================================
    print("\n   a b c d e f g h")
    for fila in range(8, 0, -1):
        linea = f"{fila} "
        for col in columnas:
            pieza = tablero[f"{col}{fila}"]
            linea += f" {simbolos[pieza]}"
        linea += f" {fila}"
        print(linea)
    print("   a b c d e f g h\n")
    
    # Mostrar el reporte actual de piezas capturadas (convertidas a símbolos ASCII)
    capturas_ascii = [simbolos[p] for p in lista_capturadas]
    print(f"Piezas capturadas: {capturas_ascii}")
    print("-" * 40)

    # Solicitar por consola el movimiento al usuario
    origen = input("Ingrese la casilla de origen (ej: e2) o 'salir': ").strip().lower()
    if origen == 'salir':
        break
        
    destino = input("Ingrese la casilla de destino (ej: e4): ").strip().lower()

    # ==========================================================================
    # e) Lógica de movimiento
    # ==========================================================================
    # Validar si las coordenadas ingresadas existen en el tablero
    if origen not in tablero or destino not in tablero:
        print("[ERROR] Una de las casillas ingresadas no es válida. Intente de nuevo.")
        continue
        
    pieza_origen = tablero[origen]
    
    # Validar si la casilla de origen tiene una pieza real
    if pieza_origen == ".":
        print("[ERROR] No hay ninguna pieza en la casilla de origen. Intente de nuevo.")
        continue

    pieza_destino = tablero[destino]

    # Verificar si en el destino hay una pieza enemiga para capturarla
    if pieza_destino != ".":
        # Se añade la pieza rival a la lista de capturadas
        lista_capturadas.append(pieza_destino)
        print(f"\n» ¡Capturó a {pieza_destino} en {destino.upper()}!")
    else:
        print(f"\n» Movimiento ejecutado de {origen.upper()} a {destino.upper()}.")

    # ==========================================================================
    # f) Reporte tras cada turno (Actualización del diccionario)
    # ==========================================================================
    # Movemos la pieza a la nueva casilla y dejamos vacía la posición anterior
    tablero[destino] = pieza_origen
    tablero[origen] = "."

print("\nSimulación finalizada. ¡Buen juego!")

