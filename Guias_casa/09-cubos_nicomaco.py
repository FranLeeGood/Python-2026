# ==============================================================================
# DESCRIPCIÓN DEL EJERCICIO:
# ==============================================================================
# Desarrollar un algoritmo que permita devolver la siguiente propiedad descubierta por
# Nicómaco de Gerasa:
# - Sumando el primer impar, se obtiene el primer cubo.
# - Sumando los dos siguientes impares, se obtiene el segundo cubo.
# - Sumando los tres siguientes impares, se obtiene el tercer cubo, y así sucesivamente.
#
# Ejemplo:
# 1³ = 1 = 1
# 2³ = 3 + 5 = 8
# 3³ = 7 + 9 + 11 = 27
# 4³ = 13 + 15 + 17 + 19 = 64
#
# Imprimir por pantalla los primeros n cubos, considerando el valor de n obtenido desde teclado.
# ==============================================================================

# Solicitar el valor de n por teclado
n = int(input("Ingrese la cantidad de cubos que quieres calcular: "))
impar = 1

# Bucle principal para controlar los n cubos
for i in range(1, n + 1):
    suma = 0
    terminos = []
    
    # Bucle interno para agrupar y sumar los números impares correspondientes
    for _ in range(i):
        suma += impar
        terminos.append(str(impar))
        impar += 2
        
    # Formatear la ecuación y mostrar el resultado en pantalla
    ecuacion = " + ".join(terminos)
    print(f"{i}³ = {ecuacion} = {suma}")

