#                   CALCULO DE LIQUIDACIONES Y BONOS
#======================================================================
# El sistema debe gestionar el registro de ventas diarias durante un 
# período de 5 días hábiles para un grupo de 3 vendedores de una tienda 
# de ropa deportiva. El objetivo es determinar las remuneraciones 
# finales sumando el sueldo legal y los incentivos comerciales.
#======================================================================
# - Venta semanal total superior a $1.500.000 (Bono de un 20 % del sueldo base)
# - Venta semanal total superior a $1.000.000 (Bono de un 10 % del sueldo base)
# - Venta semanal total superior a $500.000 (Bono de un 5 % del sueldo base)

# Además considerar: Sueldo Base en Chile 2025 es de $529.000

#Se solicita:
try:
    sueldo_base = 529000

       # a) Crea un diccionario donde la clave sea el nombre del vendedor y el
       #    valor otra estructura que guarde las ventas diarias (Puede ser una lista o tupla
    vendedores = {
        "Pedro": (300000, 400000, 250000, 350000, 300000),
        "Maria": (150000, 200000, 100000, 80000, 120000),
        "Juan": (400000, 500000, 300000, 200000, 250000)
    }

    print("=" * 60)
    print("REPORTE DE SUELDOS Y VENTAS - TIENDA DEPORTIVA")
    print("=" * 60)

    for nombre, ventas in vendedores.items():
        # b) Calcula el total de las ventas semanales de cada vendedor y su bono si le corresponde
        total_ventas = sum(ventas)
        # c) Obtener el promedio de ventas semanales de cada vendedor.
        promedio_ventas = total_ventas / len(ventas)
        
        if total_ventas > 1500000:
            porcentaje_bono = 0.20
        elif total_ventas > 1000000:
            porcentaje_bono = 0.10
        elif total_ventas > 500000:
            porcentaje_bono = 0.05
        else:
            porcentaje_bono = 0.00
            
        bono_calculado = sueldo_base * porcentaje_bono
        sueldo_total = sueldo_base + bono_calculado
        # d) Imprime un reporte con el total del sueldo a pagar por cada vendedor.
        print(f"Vendedor: {nombre}")
        print(f"  Total Ventas Semanales: ${total_ventas:,}")
        print(f"  Promedio Diario:         ${promedio_ventas:,}")
        print(f"  Porcentaje Bono:         {porcentaje_bono * 100}%")
        print(f"  Bono a Pagar:            ${bono_calculado:,}")
        print(f"  Sueldo Total Final:      ${sueldo_total:,}")
        print("-" * 60)

except Exception as e:
    print(f"Error: {e}")