manana = float(input("ingrese el consumo de ram de manana"))
print (manana)
mediodia = float(input("ingrese el consumo de ram de mediodia"))
print(mediodia)
tarde = float(input("ingrese el consumo de ram de tarde"))
print(tarde)
noche = float(input("ingrese el consumo de ram de noche"))
print(noche)

ram = [manana, mediodia, tarde, noche]
consumo_manana = ram [0]
consumo_mediodia = ram [1]
consumo_tarde = ram [2]
consumo_noche = ram [3]

consumo_total = (consumo_manana + consumo_mediodia + consumo_tarde + consumo_noche)
promedio = (consumo_total/4)


print(f"El consumo total es: {consumo_total} GB")
print(f"El consumo promedio de RAM durante el dia es: {promedio}GB")

consumo_maximo = max(ram)
consumo_minimo = min(ram)
rango_operacion = consumo_maximo - consumo_minimo

print(f"El consumo maximo detectado fue: {consumo_maximo}GB")
print(f"el consumo minimo detectado fue: {consumo_minimo}GB")
print(f"El rango de operacion del servidor es: {rango_operacion} GB")