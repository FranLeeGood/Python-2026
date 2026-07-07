# ==============================================================================
# DESCRIPCIÓN DEL EJERCICIO:
# ==============================================================================
# 7. Determinar el factorial de un número n, donde:
#    n! = n * (n - 1) * (n - 2)... * 3 * 2 * 1
# ==============================================================================

# Pedimos el número al usuario
n = int(input("Ingrese un número para calcular el factorial: "))

# Si el usuario pone un número negativo, tiramos error
if n < 0:
    print("Error: No se puede calcular el factorial de un número negativo.")
else:
    # El factorial siempre parte multiplicándose por 1
    resultado = 1
    
    # Hacemos un bucle desde 1 hasta el número que ingresó el usuario
    for i in range(1, n + 1):
        resultado = resultado * i  # Vamos multiplicando acumulado

    # Mostramos el resultado final limpito
    print(f"El factorial de {n}! es: {resultado}")
