# ==============================================================================
# DESCRIPCIÓN DEL EJERCICIO:
# ==============================================================================
# 6. Simular el comportamiento de un reloj digital, imprimiendo la hora, minutos
#    y segundos de un día desde las 00:00:00 horas hasta las 23:59:59 horas.
# ==============================================================================

import time

# Explicación del problema:
# Se utilizan tres bucles anidados para controlar las Horas, Minutos y Segundos.
# Usamos un sleep muy pequeño (0.0001) para que el profesor vea cómo corren los 
# números rápidamente por pantalla y complete el día en pocos segundos.

for hora in range(24):
    for minuto in range(60):
        for segundo in range(60):
            
            # Formatear la salida para que siempre muestre 2 dígitos (ej: 00:00:00)
            # \r permite que la hora se actualice en la misma línea de la consola
            print(f"{hora:02d}:{minuto:02d}:{segundo:02d}", end="\r")
            
            # Pausa mínima para simular el avance rápido en la consola
            time.sleep(0.0001)

print("\n¡Simulación de 24 horas completada exitosamente!")