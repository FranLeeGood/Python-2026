# =============================================================================
# DESCRIPCIÓN DEL EJERCICIO NUMERO 2

# Construir un programa que calcule e imprima la sumatoria:

# S = 500 + 456 + 510 + 454 + 520 + 452 + ... + 800
# =============================================================================
try:
    suma_total = 0
    sube = 500  
    baja = 456  
    turno_sube = True

    while sube <= 800:
        if turno_sube:
            suma_total += sube
            print(f"Se sumó: {sube} | Total acumulado: {suma_total}")
            sube += 10         
            turno_sube = False 
        else:
            suma_total += baja
            print(f"Se sumó: {baja} | Total acumulado: {suma_total}")
            baja -= 2          
            turno_sube = True  

    print("=" * 50)
    print(f"El resultado final de la sumatoria S es: {suma_total}")
    print("=" * 50)

except Exception as e:
    print(f"Error: {e}")